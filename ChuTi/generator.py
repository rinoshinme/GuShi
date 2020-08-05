import random


def get_words(filepath):
    all_words = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            words = line.strip().split(' ')
            for w in words:
                if len(w) > 0:
                    all_words.append(w)
    return all_words


def gen_triplets():
    words = get_words('./src.db')
    








