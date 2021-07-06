"""Implements audio."""

import logging

import pyttsx3

from utils import timex
from utils.cache import cache

from writing.docjson import md_to_docjson

log = logging.getLogger('writing.audio')
logging.basicConfig(level=logging.INFO)


@cache('writing.audio', timex.SECONDS_IN.YEAR)
def md_to_audio(md_file, audio_file_base):
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

        audio_file = '%s.%04d.mp3' % (audio_file_base, i)
        log.info('Saving to %s', audio_file)
        engine.save_to_file(text, audio_file)
        audio_files.append(audio_file)

    engine.runAndWait()
    return audio_files


if __name__ == '__main__':
    md_to_audio(
        'src/writing/assets/test.md',
        '/tmp/test',
    )
