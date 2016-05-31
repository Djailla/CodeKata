#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata19-word-chains/
"""

INPUT_STR = 'lead'
INPUT_STR_LEN = len(INPUT_STR)
SAME_LEN_SET = set()

DEST_STR = 'gold'


def get_close_str(input_str):
    """Generate a set of word that can be the next step in the word chain"""
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
    matching_word.remove(input_str)
    return matching_word


def get_score(scr_str, dest_str):
    """Get the proximity score with the destination word"""
    count = 0

    for i in range(INPUT_STR_LEN):
        # print '%s <=> %s' % (word[i], input_str[i])
        if scr_str[i] == dest_str[i]:
            count += 1
    return count


def get_close_score_dict(close_set, dest_str):
    """Generate a dict with words and associated score"""
    out_dict = {}
    for word in close_set:
        out_dict[word] = get_score(word, dest_str)
    return out_dict

# Basic check
if INPUT_STR_LEN != len(DEST_STR):
    print 'String %s and %s do not have the same len (%d != %d)' % (
        INPUT_STR, DEST_STR, INPUT_STR_LEN, len(DEST_STR)
    )
    exit(0)

# Copy in memory the list of words with the correct length
with open('../common/english.txt', 'r') as word_list:
    SAME_LEN_SET = set(
        word.lower().strip().replace('\'', '')
        for word in word_list.readlines()
        if len(word.lower().strip().replace('\'', '')) == INPUT_STR_LEN)

# Check if words exists
if INPUT_STR not in SAME_LEN_SET:
    print 'This word do not exists %s' % INPUT_STR
    exit(0)

if DEST_STR not in SAME_LEN_SET:
    print 'This word do not exists %s' % DEST_STR
    exit(0)


print "\n**** RESULT *****\n"

current_set = set()
new_set = get_close_str(INPUT_STR)

sorted_dict = sorted([
    (value, key)
    for (key, value)
    in get_close_score_dict(new_set, DEST_STR).items()
], reverse=True)


print "Matching words :"
for (score, word) in sorted_dict:
    print ' - %s (score : %d)' % (word, score)
print len(new_set)

# print "FOUND"
