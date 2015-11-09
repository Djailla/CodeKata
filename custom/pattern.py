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

from collections import defaultdict
from itertools import product


def is_match(pattern, test_string):
    pattern_dict = defaultdict(int)

    # Generate the pattern sizes that fit the defined pattern
    for char in list(pattern):
        pattern_dict[char] += 1

    pattern_keys = pattern_dict.keys()
    pattern_sizes = []

    for k in product(range(1, len(test_string) + 1), repeat=len(pattern_keys)):
        size = sum([idx * pattern_dict[pattern_keys[i]] for (i, idx) in enumerate(k)])
        if size == len(test_string):
            pattern_sizes.append({pattern_keys[i] : j for i, j in enumerate(k)})
    # print pattern_sizes

    # Test this patterns against the string
    for test_pattern in pattern_sizes:
        index = 0
        test_dict = defaultdict(list)

        for char in list(pattern):
            test_dict[char].append(test_string[index: index + test_pattern[char]])

            index += test_pattern[char]

        if all([len(set(value)) == 1 for value in test_dict.values()]):
            print test_dict
            return True

    return False

assert(is_match('abba', 'dogfishfishdog') is True)
assert(is_match('aba', 'dogfishdog') is True)
assert(is_match('a', 'acdefghijk') is True)
assert(is_match('ab', 'acdefghijk') is True)
assert(is_match('aba', 'dogfishfish') is False)
assert(is_match('aba', 'dogfishhorse') is False)
assert(is_match('abcba', 'dogfishhorsefishdog') is True)
