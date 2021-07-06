"""Tests for writing."""

import unittest

from writing import run_writing


class TestCase(unittest.TestCase):
    """Tests."""

    def test_dump(self):
        """Test."""
        self.assertTrue(run_writing._dump())


if __name__ == '__main__':
    unittest.main()
