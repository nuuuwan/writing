"""Implements audio."""

import argparse
import logging
import os

import pyttsx3
from pydub import AudioSegment

from writing.docjson import md_to_docjson

log = logging.getLogger('writing.audio')
logging.basicConfig(level=logging.INFO)


def combine_audios(audio_files, combined_audio_file):
    """Combined audiofiles into single audio."""
    combined_segment = None
    for audio_file in audio_files:
        segment = AudioSegment.from_file(
            audio_file,
            'aiff',
        )
        if combined_segment is None:
            combined_segment = segment
        else:
            combined_segment += segment
        os.system('rm %s' % audio_file)

    combined_segment.export(
        combined_audio_file,
        format='aiff',
    )
    log.info('Saved combined audios to %s', combined_audio_file)


def md_to_audio(md_file, audio_file_base, combined_audio_file):
    """Convert MD to audio."""
    docjson = md_to_docjson(md_file)

    engine = pyttsx3.init()
    audio_files = []
    for i, d in enumerate(docjson):
        text = d['text']
        tag = d['tag']

        if tag == 'p':
            engine.setProperty('rate', 225)
            engine.setProperty(
                'voice',
                'com.apple.speech.synthesis.voice.Kate',
            )
        else:
            engine.setProperty('rate', 200)
            engine.setProperty(
                'voice',
                'com.apple.speech.synthesis.voice.Daniel',
            )

        audio_file = '%s.%04d.aiff' % (audio_file_base, i)
        log.info('Saving to %s', audio_file)
        engine.save_to_file(text, audio_file)
        audio_files.append(audio_file)
    engine.runAndWait()

    if combined_audio_file:
        combine_audios(audio_files, combined_audio_file)
    return audio_files


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Writing-Audio')
    parser.add_argument('md-filename')
    args = vars(parser.parse_args())
    _md_file = args.get('md-filename')
    _audio_file_base = _md_file.replace('.md', '')
    _combined_audio_file = _md_file.replace('.md', '.aiff')
    print(_combined_audio_file)
    md_to_audio(_md_file, _audio_file_base, _combined_audio_file)
