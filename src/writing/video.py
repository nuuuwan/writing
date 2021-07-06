"""Implements video."""

import logging

from moviepy.editor import TextClip, concatenate

from writing.docjson import md_to_docjson

log = logging.getLogger('writing.video')
logging.basicConfig(level=logging.INFO)


def _break_text(text):
    words = text.split(' ')
    lines = []
    for word in words:
        if not lines or len(' '.join(lines[-1])) > 50:
            lines.append([])
        lines[-1].append(word)
    return '\n'.join(list(map(
        lambda line: ' '.join(line),
        lines,
    )))


def md_to_video(md_file, video_file=None):
    if video_file is None:
        video_file = md_file.replace('.md', '.mp4')
    docjson = md_to_docjson(md_file)

    text_clips = []
    for d in docjson:
        text_clip = TextClip(
            _break_text(d['text']),
            fontsize=32,
            color='black',
            bg_color='white',
            size=(1600, 900),
        ).set_position('center').set_duration(1)
        text_clips.append(text_clip)

    composite_clip = concatenate(text_clips, method='compose')
    composite_clip.write_videofile(video_file, fps=25)
    log.info('Wrote %s to %s', md_file, video_file)


if __name__ == '__main__':
    md_to_video(
        'src/writing/assets/test.md',
    )
