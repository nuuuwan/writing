"""Implements docjson."""


from utils import filex


def md_line_to_docjson(line):
    """Convert MD line to DocJSON."""
    tag = 'p'
    text = line
    for i in range(1, 10):
        header_text = ('#' * (i)) + ' '
        if line[:i + 1] == header_text:
            tag = 'h%d' % i
            text = line[i + 1:]
            break

    return {
        'tag': tag,
        'text': text,
    }


def md_to_docjson(md_file, docjson_file=None):
    """Convert MD file to DocJSON."""
    if docjson_file is None:
        docjson_file = md_file.replace('.md', '.doc.json')
    lines = filex.read(md_file).split('\n')

    docjson = list(map(md_line_to_docjson, lines))
    return docjson


if __name__ == '__main__':
    md_to_docjson(
        'src/writing/assets/test.md',
    )
