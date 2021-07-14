"""Implements video."""

import argparse
import logging
import os

from moviepy.editor import AudioFileClip, TextClip, concatenate

from writing.audio import md_to_audio
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
    return '\n'.join(
        list(
            map(
                lambda line: ' '.join(line),
                lines,
            )
        )
    )


def md_to_video(md_file, video_file=None, do_clean=True):
    if video_file is None:
        video_file = md_file.replace('.md', '.mp4')
    audio_file_base = video_file.replace('.mp4', '')
    docjson = md_to_docjson(md_file)
    combined_audio_file = None
    audio_files = md_to_audio(md_file, audio_file_base, combined_audio_file)

    frame_clips = []
    for d, audio_file in zip(docjson, audio_files):
        audio_clip = AudioFileClip(audio_file)

        text_clip = (
            TextClip(
                _break_text(d['text']),
                fontsize=32,
                color='black',
                bg_color='white',
                font='Monaco',
                size=(1600, 900),
            )
            .set_position('center')
            .set_duration(audio_clip.duration)
            .set_audio(audio_clip)
        )

        frame_clips.append(text_clip)

    video_clip = concatenate(frame_clips, method='compose')
    video_clip.write_videofile(video_file, fps=3)
    log.info('Wrote %s to %s', md_file, video_file)

    if do_clean:
        os.system('rm -rf %s*aiff*' % (audio_file_base))
        log.info('Cleaned audio files')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Writing-Video')
    parser.add_argument('md-filename')
    args = vars(parser.parse_args())
    _md_file = args.get('md-filename')
    file_base = _md_file.split('/')[-1].replace('.md', '')
    _video_file_name = '/Users/nuwan.senaratna/Desktop/%s.mp4' % file_base
    md_to_video(_md_file, _video_file_name)
