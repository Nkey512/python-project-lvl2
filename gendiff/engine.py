from gendiff.statuses import SAVED, REMOVED, ADDED, CHILD, FROM, TO
from textwrap import indent


SIGN = {
    SAVED: ' ',
    REMOVED: '-',
    ADDED: '+',
    CHILD: ' ',
    FROM: '-',
    TO: '+'
    }


def build_diff(doc1, doc2):
    x = set(doc1.keys())
    y = set(doc2.keys())
    result = {}
    all_keys = tuple(sorted(x | y))
    only_1keys = x - y
    only_2keys = y - x
    both_keys = x & y
    for key in all_keys:
        if key in only_1keys:
            result[key] = (REMOVED, doc1[key])
        if key in only_2keys:
            result[key] = (ADDED, doc2[key])
        if key in both_keys:
            result[key] = compare_children(doc1[key], doc2[key])
    return result


def compare_children(elem1, elem2):
    if elem1 == elem2:
        return SAVED, elem1
    elif isinstance(elem1, dict) \
            and isinstance(elem2, dict) \
            and elem1 != elem2:
        return CHILD, build_diff(elem1, elem2)
    elif not (isinstance(elem1, dict) and isinstance(elem2, dict)):
        return FROM, elem1, TO, elem2


def norm_dict(x, curr_ind=4):
    if isinstance(x, dict):
        s = ''
        for key, value in x.items():
            s += '{}{}: {}\n'.format((curr_ind+2)*' ', key, norm_dict(value, curr_ind=curr_ind+4))
        return '{\n' + s + (curr_ind-2)*' ' + '}'
    return x


def stylish(diff):

    def rec_style(d):
        body_indent = 4
        tail_indent = 2
        string = ''''''
        for k, v in d.items():
            if v[0] != CHILD:
                curr_str = '{} {}: {}\n'.format(SIGN[v[0]], k, norm_dict(v[1]))
                string += curr_str
                if len(v) == 4:
                    curr_str = '{} {}: {}\n'.format(SIGN[v[2]], k, norm_dict(v[3]))
                    string += curr_str
            else:
                curr_str = '{} {}: {}\n'.format(SIGN[v[0]], k, '{')
                string += curr_str
                curr_str = rec_style(v[1])
                string += indent(curr_str, body_indent*' ')
                curr_str = '}\n'
                string += indent(curr_str, tail_indent*' ')
        return string

    return '{\n' + indent(rec_style(diff), '  ') + '}'
