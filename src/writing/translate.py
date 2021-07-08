"""Implements translate."""

import logging

import nltk
from deep_translator import GoogleTranslator
from utils import filex, timex
from utils.cache import cache

log = logging.getLogger('writing.translate')
logging.basicConfig(level=logging.INFO)
translator = GoogleTranslator(source='english', target='sinhala')


@cache('writing.translate', timex.SECONDS_IN.YEAR)
def translate(text):
    """Translate text."""
    return translator.translate(text)


def translate_md(md_file, translated_md_file):
    """Translate md file."""
    lines = filex.read(md_file).split('\n')
    lines_with_sentences = list(map(nltk.sent_tokenize, lines))

    translated_lines_with_sentences = []
    for line_sentences in lines_with_sentences:
        translated_line_sentences = []
        for sentence in line_sentences:
            translated_line_sentences.append(translate(sentence))
        translated_lines_with_sentences.append(translated_line_sentences)

    translated_lines = list(
        map(
            lambda translated_line_sentences: ' '.join(
                translated_line_sentences
            ),
            translated_lines_with_sentences,
        )
    )
    filex.write(translated_md_file, '\n'.join(translated_lines))
    log.info('Translated %s as %s', md_file, translated_md_file)


if __name__ == '__main__':
    translate_md(
        'src/writing/assets/the-solutionists-manifesto.md',
        '/tmp/the-solutionists-manifesto.si.md',
    )
