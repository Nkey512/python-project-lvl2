# -*- coding:utf-8 -*-

"""gendiff function representation tests."""

from gendiff.scripts.gendiff import generate_diff


string = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

path1 = 'tests/fixtures/file1.json'
path2 = 'tests/fixtures/file2.json'


def test_flat_json():
    assert generate_diff(path1, path2) == string


path3 = 'tests/fixtures/file3.yml'
path4 = 'tests/fixtures/file4.yml'


def test_flat_yaml():
    assert generate_diff(path3, path4) == string
