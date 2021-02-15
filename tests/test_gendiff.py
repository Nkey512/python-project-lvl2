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
}
'''


def test_flat_json():
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == string


def test_flat_yaml():
    assert generate_diff('tests/fixtures/file1.yml',
                         'tests/fixtures/file2.yml') == string
