import glob
import re


def list_relations():
    return glob.glob('relations/*.txt')


def read_relations(path_to_file):
    list_pairs = []
    with open(path_to_file, 'r') as relations:
        relations = relations.readlines()[1:]
        for pair in relations:
            pair = re.sub(r'[^a-zA-Z, ]', '', pair)
            list_pairs.append(tuple(pair.split(',')))
        return list_pairs


if __name__ == '__main__':
    print(list_relations())
    for path in list_relations():
        print(read_relations(path))
