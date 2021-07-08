"""Implements docjson."""

import logging

from utils import filex

log = logging.getLogger('writing.docjson')
logging.basicConfig(level=logging.INFO)


def md_line_to_docjson(line):
    """Convert MD line to DocJSON."""
    tag = 'p'
    text = line
    for i in range(1, 10):
        header_text = ('#' * (i)) + ' '
        if line[: i + 1] == header_text:
            tag = 'h%d' % i
            text = line[i + 1 :]
            break

    return {
        'tag': tag,
        'text': text,
    }


def md_to_docjson(md_file):
    """Convert MD file to DocJSON."""
    lines = filex.read(md_file).split('\n')

    docjson = list(map(md_line_to_docjson, lines))
    docjson = list(filter(lambda d: len(d['text']) > 0, docjson))
    log.info('Converted %s into DocJSON', md_file)
    return docjson


if __name__ == '__main__':
    md_to_docjson('src/writing/assets/test.md')
