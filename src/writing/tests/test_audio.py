"""Tests for writing."""

import unittest

from writing import audio


class TestCase(unittest.TestCase):
    """Tests."""

    def test_dump(self):
        """Test."""
        self.assertTrue(audio.md_to_audio('', ''))


if __name__ == '__main__':
    unittest.main()
