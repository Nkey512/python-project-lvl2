# -*- coding:utf-8 -*-

"""gendiff function representation tests."""

from gendiff.scripts.gendiff import generate_diff


def test_flat_json():
    string = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
'''
    assert generate_diff('fixtures/file1.json', 'fixtures/file2.json') == string


test_flat_json()
