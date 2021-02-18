#!usr/bin/env python
from gendiff.parsing import parse_file


def diff(doc1, doc2):
    return


def stylish(tree, tab=2):
    return


def generate_diff(file1, file2, formatter=stylish):
    inner_d = diff(file1, file2)
    return formatter(inner_d)


def main():
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        metavar='FORMAT')
    args = parser.parse_args()
    file1 = parse_file(args.first_file)
    file2 = parse_file(args.second_file)
    sys.stdout.write(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
