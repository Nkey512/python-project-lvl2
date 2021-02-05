#!usr/bin/env python
def main():
    import argparse
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        metavar='FORMAT')
    args = parser.parse_args()
    print(args)
    print('Hello World!')


if __name__ == '__main__':
    main()
