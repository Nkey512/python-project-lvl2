from gendiff.statuses import SAVED, REMOVED, ADDED, CHILD, FROM, TO


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


def pretty_dict(x):
    if isinstance(x, dict):
        res = []
        for key, value in x.items():
            res.append('{}: {}'.format(key, pretty_dict(value)))
        return '{\n' + '\n'.join(res) + '\n}'
    return x


def stylish(diff):
    string = ''
    for key, value in diff.items():
        if value[0] == CHILD:
            string += '{} {}: '.format(SIGN[value[0]], key)
            string += '{\n'
            for k, v in value[1].items():
                if v[0] == CHILD:
                    string += stylish(v[1])
                elif len(v) == 2:
                    string += '{} {}: {}\n'.format(SIGN[v[0]], k, pretty_dict(v[1]))
                elif len(v) == 4:
                    string += '{} {}: {}\n'.format(SIGN[v[0]], k, pretty_dict(v[1]))
                    string += '{} {}: {}\n'.format(SIGN[v[2]], k, pretty_dict(v[3]))
            string += '}\n'
        else:
            string += '{} {}: {}\n'.format(SIGN[value[0]], key, pretty_dict(value[1]))
    return string
