#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata19-word-chains/
"""

from collections import defaultdict
import unicodedata

INPUT_STR = 'presse'
INPUT_STR_LEN = len(INPUT_STR)
SAME_LEN_SET = set()


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


def get_close_str(input_str):
    matching_word = set()

    for word in SAME_LEN_SET:
        count = 0
        for i in range(INPUT_STR_LEN):
            # print '%s <=> %s' % (word[i], input_str[i])
            if word[i] != input_str[i]:
                count += 1
                if count >= 2:
                    break
        if count >= 2:
            continue
        matching_word.add(word)
    return matching_word

with open('../common/french.txt', 'r') as word_list:
    SAME_LEN_SET = set(
        strip_accents(
            to_unicode(
                word.strip().replace('\'', '').lower()
            )
        )
        for word in word_list.readlines()
        if len(to_unicode(word.strip())) == INPUT_STR_LEN)

print "\n**** RESULT *****\n"

current_set = set()
new_set = get_close_str(INPUT_STR)

print "Matching words :"
for word in new_set:
    print ' - %s' % word
print len(new_set)


# iteration = 0
# while new_set != current_set:
#     iteration += 1
#     print "Iteration %d" % iteration

#     current_set = new_set.copy()
#     new_set = set()
#     for word in current_set:
#         new_set.update(get_close_str(word))

#     print "Word set:"
#     for word in new_set:
#         print ' - %s' % word
#     print len(new_set)
