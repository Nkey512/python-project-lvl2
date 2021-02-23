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

string2 = '''{
    common: {
      + follow: False
        setting1: Value 1
      - setting2: 200
      - setting3: True
      + setting3: None
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''  # noqa W291

path1 = 'tests/fixtures/file1.json'
path2 = 'tests/fixtures/file2.json'
path3 = 'tests/fixtures/file3.yml'
path4 = 'tests/fixtures/file4.yml'
path5 = 'tests/fixtures/rec1.json'
path6 = 'tests/fixtures/rec2.json'
path7 = 'tests/fixtures/rec3.yml'
path8 = 'tests/fixtures/rec4.yml'


def test_flat_json():
    assert generate_diff(path1, path2) == string


def test_flat_yaml():
    assert generate_diff(path3, path4) == string


def test_rec_json():
    assert generate_diff(path5, path6) == string2


def test_rec_yaml():
    assert generate_diff(path7, path8) == string2
