import sys
from utils import filex

def print_word_count(file_name):
    words = filex.read(file_name).split(' ')
    print('Word Count = %d' % len(words))

if __name__ == '__main__':
    file_name = sys.argv[1]
    print_word_count(file_name)
