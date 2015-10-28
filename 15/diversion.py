#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata15-a-diversion/

The answer for the last question is :

n = (n-1) + (n-2)
"""

import itertools


def get_items(item_size):
    allorderings = itertools.product(['0', '1'], repeat=item_size)

    my_list = []

    for item in allorderings:
        if not '11' in ''.join(item):
            my_list.append(''.join(item))

    print "For %d element, the list size is %d" % (item_size, len(my_list))

for n in xrange(1, 11):
    get_items(n)