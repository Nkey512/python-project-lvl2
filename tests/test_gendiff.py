# -*- coding:utf-8 -*-

"""gendiff function representation tests."""

from gendiff.scripts.gendiff import generate_diff
from gendiff.parsing import parse_file

string = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
'''
file1 = parse_file('tests/fixtures/file1.json')
file2 = parse_file('tests/fixtures/file2.json')


def test_flat_json():
    assert generate_diff(file1, file2) == string


file3 = parse_file('tests/fixtures/file3.yml')
file4 = parse_file('tests/fixtures/file4.yml')


def test_flat_yaml():
    assert generate_diff(file3, file4) == string
