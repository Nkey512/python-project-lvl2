#!usr/bin/env python
from gendiff import parsing
from gendiff.cli import cli_argparser
from gendiff.engine import build_diff, stylish


def generate_diff(file1, file2, formatter=stylish):
    parsed_file1 = parsing.get_data(file1)
    parsed_file2 = parsing.get_data(file2)
    inner_d = build_diff(parsed_file1, parsed_file2)
    return formatter(inner_d)


def main():
    args = cli_argparser().parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
