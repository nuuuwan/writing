"""Uploaded data to nuuuwan/writing:data branch."""

import os


def upload_data():
    """Upload data."""
    os.system('echo "test data" > /tmp/writing.test.txt')
    os.system('echo "# writing" > /tmp/README.md')


if __name__ == '__main__':
    upload_data()
