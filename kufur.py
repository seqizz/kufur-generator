#!/usr/bin/env python3

import random


def find_one_random(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()
        random_int = random.randint(0, len(lines) - 1)
        return lines[random_int].rstrip()


def find_last_vowel(word):
    vowels = set('aeıiouöü')

    for idx, item in enumerate(word[::-1], 1):
        if item in vowels:
            return item

    raise ValueError('no vowels found, should not happen')


def format_suffix(direction, chosen_thing):

    if find_last_vowel(chosen_thing) in 'aıou':
        if direction:
            return 'da'
        return 'a'

    if direction:
        return 'de'
    return 'e'


def kufur():
    # Pick  the special full-sentence ones (lower probability)
    if bool(random.choices(population=[0, 1], weights=[4, 1], k=1)[0]):
        return find_one_random('data/ozel_kufurler')

    direction = not bool(random.getrandbits(1))
    chosen_thing = find_one_random('data/hedefler')

    # Add extra spice
    chosen_adjective = ''
    if bool(random.getrandbits(1)):
        chosen_adjective = '{} '.format(find_one_random('data/sifatlar'))

    return('{}{}{} {}{} {}'.format(
        'senin ' if bool(random.getrandbits(1)) else '',
        chosen_adjective,
        find_one_random('data/kisiler'),
        chosen_thing,
        format_suffix(direction, chosen_thing),
        find_one_random('data/da-kufurler') if direction else find_one_random('data/a-kufurler'),
    ))


if __name__ == "__main__":
    print(kufur())
