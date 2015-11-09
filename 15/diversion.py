#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata15-a-diversion/

The answer for the last question is :

n = (n-1) + (n-2)

n - 1 => All starting with 0
n - 2 => All starting with 10
"""

import itertools


def check_input(func):
    def check_input_wrap(*args, **kwargs):
        """wrapper"""
        if args[0] < 1:
            return 0
        else:
            return func(*args, **kwargs)
    return check_input_wrap


@check_input
def get_items1(item_size):
    """Using string compare we can look for the pattern in the string"""
    item_count = sum(1 for item in
                     itertools.product(['0', '1'], repeat=item_size)
                     if not '11' in ''.join(item)
                     )
    return item_count


@check_input
def get_items2(item_size):
    """Trying to use Boolean instead of strings"""
    range_size = range(item_size - 1)

    item_count = sum(1 for item in
                     itertools.product([False, True], repeat=item_size)
                     if not sum((item[i] and item[i+1] and 1 or 0) for i in range_size)
                     )
    return item_count


@check_input
def get_items3(item_size):
    """Using the real expression to calculate final value"""
    item_list = [1, 2, 3]

    if item_size < len(item_list):
        return item_list[item_size]

    for n in range(item_size - 2):
        item_list.append(item_list[-1] + item_list[-2])

    return item_list[-1]


def do_it(n):
    for x in range(100):
        get_items1(n)


def do_it2(n):
    for x in range(100):
        get_items2(n)


def do_it3(n):
    for x in range(100):
        get_items3(n)


for n in xrange(-3, 20):
    print "get_items1 : For %d element, the list size is %d" % (n, get_items1(n))
    print "get_items2 : For %d element, the list size is %d" % (n, get_items2(n))
    print "get_items3 : For %d element, the list size is %d" % (n, get_items3(n))

# import profile
# profile.run('do_it(10)')
# profile.run('do_it3(10)')
