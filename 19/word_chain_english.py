#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata19-word-chains/
"""
from Queue import PriorityQueue
DEST_STR = 'gold'
INPUT_STR = 'lead'
INPUT_STR_LEN = len(INPUT_STR)
SAME_LEN_SET = set()


def get_close_str(input_str):
    """Generate a set of word that can be the next step in the word chain"""
    matching_words = set()

    for word in SAME_LEN_SET:
        count = 0
        for i in range(INPUT_STR_LEN):
            if word[i] != input_str[i]:
                count += 1
                if count >= 2:
                    break
        if count >= 2:
            continue
        matching_words.add(word)
    matching_words.remove(input_str)
    return matching_words


def get_score(scr_str, dest_str):
    """Get the proximity score with the destination word"""
    count = 0

    for i in range(INPUT_STR_LEN):
        if scr_str[i] == dest_str[i]:
            count += 1
    return count

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


word_queue = PriorityQueue()
word_queue.put(INPUT_STR, 0)
came_from = {}
came_from[INPUT_STR] = None

while not word_queue.empty():
    current = word_queue.get()

    if current == DEST_STR:
        break

    for new_word in get_close_str(current):
        if new_word not in came_from:
            score = get_score(new_word, DEST_STR)
            word_queue.put(new_word, score)
            came_from[new_word] = current

current = DEST_STR
path = [current]
while current != INPUT_STR:
    current = came_from[current]
    path.append(current)
path.reverse()

print '\n'.join(path)
