#!usr/bin/env python
import json
import argparse


def generate_diff(file_path1, file_path2):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        metavar='FORMAT')
    args = parser.parse_args()
    print(args)
    print('Hello World!')


def main():
    generate_diff()


if __name__ == '__main__':
    main()
