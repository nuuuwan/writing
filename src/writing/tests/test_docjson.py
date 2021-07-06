"""Tests for writing."""

import unittest

from writing import docjson


class TestCase(unittest.TestCase):
    """Tests."""

    def test_md_line_to_docjson(self):
        """Test."""
        for line, exp_docjson in [
            [
                '# Heading 1',
                {
                    'tag': 'h1',
                    'text': 'Heading 1',
                }
            ],
            [
                'Paragraph text',
                {
                    'tag': 'p',
                    'text': 'Paragraph text',
                }
            ],
        ]:
            self.assertEqual(
                exp_docjson,
                docjson.md_line_to_docjson(line),
            )


if __name__ == '__main__':
    unittest.main()
