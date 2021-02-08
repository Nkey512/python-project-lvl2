#!usr/bin/env python
import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys1 = set(list(file1))
    keys2 = set(list(file2))
    all_keys = tuple(sorted({*keys1, *keys2}))
    only_in_keys1 = keys1.difference(keys2)
    only_in_keys2 = keys2.difference(keys1)
    output = []
    for key in all_keys:
        if key in only_in_keys1:
            output.append('  - {}: {}'.format(key, file1[key]))
        elif key in only_in_keys2:
            output.append('  + {}: {}'.format(key, file2[key]))
        else:
            value1 = file1[key]
            value2 = file2[key]
            if value1 == value2:
                output.append('    {}: {}'.format(key, value1))
            else:
                output.append('  - {}: {}'.format(key, value1))
                output.append('  + {}: {}'.format(key, value2))
    return '{\n' + '\n'.join(output) + '\n}\n'


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
    sys.stdout.write(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
