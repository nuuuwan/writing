"""Tests for writing."""

import unittest

from writing import translate


class TestCase(unittest.TestCase):
    """Tests."""

    def test_translate(self):
        """Test."""
        for word, expectedTranslation in [
            ['Sinhala', 'සිංහල'],
            ['People', 'සෙනඟ'],
            [
                'The boy stood on the burning deck.',
                'පිරිමි ළමයා දැවෙන තට්ටුව මත සිටගෙන සිටියේය.',
            ],
            ['Programming Language', 'ක්‍රමලේඛන භාෂාව'],
        ]:
            self.assertEqual(
                expectedTranslation,
                translate.translate(word),
            )


if __name__ == '__main__':
    unittest.main()
