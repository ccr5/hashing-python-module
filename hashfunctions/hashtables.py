import operator as op
import itertools as ittls
from .hashfunctions import alphanumeric_hash_function, numeric_hash_function


def hash_table_alphanumeric(data, key_index):

    n = len(data)
    key_list = [x for x in [
        list(vec.keys())[0]
        for vec in data
    ]]

    hash_gen = map(alphanumeric_hash_function,
                   key_list, ittls.repeat(n))

    ret = list(range(n))
    for i in iter(data):
        index = next(hash_gen)

        if type(ret[index]) == list:
            ret[index].append(i)
        else:
            ret[index] = [i]

    print(ret)
    return ret


def hash_table_numeric(data, key_index):
    n = len(data)
    for vec in iter(data):
        yield numeric_hash_function(data[index], n)
