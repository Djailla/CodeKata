#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Given a pattern and a string, return a boolean of whether the string matches the pattern.
Each character in pattern represents one of more characters in string.

Method: is_match(pattern, string)

Sample Testcases :
is_match('abba', 'dogfishfishdog') -> True
is_match('aba', 'dogfishdog') -> True
is_match('a', 'acdefghijk') -> True
is_match('ab', 'acdefghijk') -> True

is_match('aba', 'dogfishfish') -> False
is_match('aba', 'dogfishhorse') -> False


Preferable use Python, and say the Big O runtime and space.
"""

from collections import defaultdict, Counter
from itertools import product


def is_match(pattern, test_string):
    # Generate the pattern map that count the occurence of element in the pattern
    pattern_counter = Counter(pattern)

    # From now we now how many element of the pattern to retreive in the string
    pattern_keys = pattern_counter.keys()
    pattern_sizes = []

    test_string_len = len(test_string)
    pattern_keys_len = len(pattern_keys)

    # Iterate on every possibility of element size to fit the pattern
    for k in product(range(1, test_string_len - pattern_keys_len + 2),
                     repeat=pattern_keys_len):

        size = sum([idx * pattern_counter[pattern_keys[i]] for (i, idx) in enumerate(k)])

        # If the size fit, keep a copy of this compositon of elements
        if size == test_string_len:
            pattern_sizes.append({pattern_keys[i] : j for i, j in enumerate(k)})

    # Then tests thes patterns against the string
    for test_pattern in pattern_sizes:
        index = 0
        # Using defaultdict, each value of the dict will contains the
        # the extracted string from the input with the size defined in the
        # pattern
        test_dict = defaultdict(list)

        for char in list(pattern):
            test_dict[char].append(test_string[index: index + test_pattern[char]])
            index += test_pattern[char]

        # If all the list of the default dict contains identical values
        # it means that this pattern fit !
        if all([len(set(value)) == 1 for value in test_dict.values()]):
            print test_dict.items()
            return True

    return False

assert(is_match('abba', 'dogfishfishdog') is True)
assert(is_match('aba', 'dogfishdog') is True)
assert(is_match('a', 'acdefghijk') is True)
assert(is_match('ab', 'acdefghijk') is True)
assert(is_match('aba', 'dogfishfish') is False)
assert(is_match('aba', 'dogfishhorse') is False)
assert(is_match('abcba', 'dogfishhorsefishdog') is True)
assert(is_match('aaaaa', 'marcmarcmarcmarcmarc') is True)
assert(
    is_match(
        'aaaaabbbbb',
        'marcmarcmarcmarcmarcbobbobbobbobbob'
    ) is True
)


def do_it():
    for i in xrange(50):
        is_match('abcba', 'dogfishhorsefishdog')

import profile
profile.run('do_it()')
