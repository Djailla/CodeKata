#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata06-anagrams/
"""

from collections import defaultdict

with open('wordlist.txt', 'r') as word_list:
    d = defaultdict(list)

    for word in word_list.readlines():
        stripped_word = word.strip()
        d[''.join(sorted(stripped_word.replace('\'', '').lower()))].append(stripped_word)

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

    for value in max_num_list:
        print ' - '.join(value)
    print len(max_num_list[0])

    for value in max_len_list:
        print ' - '.join(value)
    print len(max_len_list[0][0])
