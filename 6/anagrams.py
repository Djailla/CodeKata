#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata06-anagrams/
"""

from collections import defaultdict
import unicodedata


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def to_unicode(data):
    """
    Convert data entry to unicode
    """
    if type(data) == unicode:
        return data
    else:
        return data.decode('utf-8')

with open('french.txt', 'r') as word_list:
    d = defaultdict(list)

    for word in word_list.readlines():
        stripped_word = word.strip()
        d[''.join(
            sorted(
                strip_accents(
                    to_unicode(
                        stripped_word.replace('\'', '').lower()
                    )
                )
            )
        )].append(stripped_word)

    max_num = 0
    max_num_list = []

    max_len = 0
    max_len_list = []
    for key, value in d.iteritems():
        value_counter = len(value)
        len_counter = len(key)

        if value_counter > 1:
            if value_counter == max_num:
                max_num_list.append(value)
            elif value_counter > max_num:
                max_num = value_counter
                max_num_list = [value]

            if len_counter == max_len:
                max_len_list.append(value)
            elif len_counter > max_len:
                max_len = len_counter
                max_len_list = [value]

            print " - ".join(value)

    print "\n**** RESULT *****\n"

    print "Longest list :"
    for value in max_num_list:
        print ' - '.join(value)
    print len(max_num_list[0])

    print "\nLongest word :"
    for value in max_len_list:
        print ' - '.join(value)
    print len(max_len_list[0][0])
