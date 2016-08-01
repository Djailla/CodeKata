#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata19-word-chains/
"""

import search_algo
from optparse import OptionParser
import unicodedata
import sys


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


def get_clean_word(word):
    return strip_accents(
        to_unicode(word).strip().replace('\'', '').lower()
    )


def main(lang, algo, word1, word2):
    word_set = set()
    word_dict = {}

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

    dict_path = {
        'en': '../common/english.txt',
        'fr': '../common/french.txt'
    }

    # Copy in memory the list of words with the correct length
    with open(dict_path[lang], 'r') as word_list:
        for word in word_list.readlines():
            clean_word = get_clean_word(word)
            if len(clean_word) == len_clean_word1:
                word_set.add(clean_word)
                # Store clean_word / real_word association for final display
                word_dict[clean_word] = word.strip()

    # Check if words exists
    if clean_word1 not in word_set:
        print 'This word do not exists %s' % clean_word1
        return

    if clean_word2 not in word_set:
        print 'This word do not exists %s' % clean_word2
        return

    # Find path using correct algorithm
    path = search_algo.get_path(clean_word1, clean_word2, algo, word_set)
    if not path:
        print 'No word chain found for this words'
        sys.exit(0)

    # Recreate the path with 'full words' instead of cleaned ones
    real_words = [word_dict[word] for word in path]

    # Print output
    print ' -> '.join(real_words)

if __name__ == "__main__":
    usage = "usage: %prog [options] word1 word2"

    parser = OptionParser(usage=usage)
    parser.add_option(
        "-l", "--lang", dest="langugage", default="en",
        help="Language of the dictionnary to use (fr / en)")
    parser.add_option(
        "-a", "--algo", dest="algo", default="astar",
        help="Search algorithm to to (astar / greedy / dijkstra)")

    (options, args) = parser.parse_args()
    if options.langugage not in ['en', 'fr']:
        print 'Lang %s not available' % options.langugage
        sys.exit(0)

    if options.algo not in ['astar', 'greedy', 'dijkstra']:
        print 'Algo %s not available' % options.algo
        sys.exit(0)

    if len(args) != 2:
        print 'Missing or extra args, must be only 2 words'

    main(options.langugage, options.algo, args[0], args[1])
