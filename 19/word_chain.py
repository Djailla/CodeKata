#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata19-word-chains/
"""

import heapq
from optparse import OptionParser
import unicodedata
import sys


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


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


def get_close_str(input_str, input_len, word_set):
    """Generate a set of word that can be the next step in the word chain"""
    matching_words = set()

    for word in word_set:
        count = 0
        for i in range(input_len):
            if word[i] != input_str[i]:
                count += 1
                if count >= 2:
                    break
        if count >= 2:
            continue
        matching_words.add(word)
    matching_words.remove(input_str)
    return matching_words


def get_score(scr_str, dest_str, word_len):
    """Get the proximity score with the destination word"""
    count = word_len

    for i in range(word_len):
        if scr_str[i] == dest_str[i]:
            count -= 1
    return count


def get_clean_word(word):
    return strip_accents(
        to_unicode(word).strip().replace('\'', '').lower()
    )


def main(lang, word1, word2):
    word_set = set()

    clean_word1 = get_clean_word(word1)
    len_clean_word1 = len(clean_word1)
    clean_word2 = get_clean_word(word2)
    len_clean_word2 = len(clean_word2)

    # Basic check
    if len_clean_word1 != len_clean_word2:
        print 'String %s and %s do not have the same len (%d != %d)' % (
            clean_word1, clean_word2, len_clean_word1, len_clean_word2
        )
        return

    # # Copy in memory the list of words with the correct length
    # with open('../common/english.txt', 'r') as word_list:
    #     word_set = set(
    #         word.lower().strip().replace('\'', '')
    #         for word in word_list.readlines()
    #         if len(word.lower().strip().replace('\'', '')) == INPUT_STR_LEN
    #     )

    dict_path = {
        'en': '../common/english.txt',
        'fr': '../common/french.txt'
    }

    # Copy in memory the list of words with the correct length
    with open(dict_path[lang], 'r') as word_list:
        for word in word_list.readlines():
            clean_word = strip_accents(
                to_unicode(word).strip().replace('\'', '').lower()
            )
            if len(clean_word) == len_clean_word1:
                word_set.add(clean_word)

    # Check if words exists
    if clean_word1 not in word_set:
        print 'This word do not exists %s' % clean_word1
        return

    if clean_word2 not in word_set:
        print 'This word do not exists %s' % clean_word2
        return

    word_queue = PriorityQueue()
    word_queue.put(clean_word1, 0)
    came_from = {}
    cost_so_far = {}
    came_from[clean_word1] = None
    cost_so_far[clean_word1] = 0

    while not word_queue.empty():
        current = word_queue.get()

        if current == clean_word2:
            break

        for next in get_close_str(current, len_clean_word1, word_set):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + get_score(next, clean_word2, len_clean_word1)
                word_queue.put(next, priority)
                came_from[next] = current

    current = clean_word2
    path = [current]
    while current != clean_word1:
        current = came_from[current]
        path.append(current)
    path.reverse()

    print ' -> '.join(path)

if __name__ == "__main__":
    usage = "usage: %prog [options] word1 word2"

    parser = OptionParser(usage=usage)
    parser.add_option(
        "-l", "--lang", dest="langugage", default="en",
        help="Language of the dictionnary to use (fr / en)")

    (options, args) = parser.parse_args()
    dict_lang = 'en'
    if options.langugage:
        if options.langugage in ['en', 'fr']:
            dict_lang = options.langugage
        else:
            print 'Lang %s not available' % options.langugage
            sys.exit(0)

    if len(args) != 2:
        print 'Missing or extra args, must be only 2 words'

    main(dict_lang, args[0], args[1])
