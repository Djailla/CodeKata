#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Resolving this question :
http://www.careercup.com/question?id=5879102479269888

Check given Number is same after 180 degree rotation?

i/p: 69
o/p: True

i/p: 916
o/p: True

i/p: 123
o/p: False
"""

import random

ALL_DIGIT = range(0, 10)

MATCH_SIDE = {
    0: 0,
    1: 1,
    6: 9,
    8: 8,
    9: 6,
}
MATCH_EXTREMITY = list(set(MATCH_SIDE.keys()) - set([0]))
MATCH_MIDDLE = [0, 1, 8]

BAD_SIDE = list(set(ALL_DIGIT) - set(MATCH_SIDE.keys()))
BAD_EXTREMITY = list(set(BAD_SIDE) - set(MATCH_EXTREMITY))
BAD_MIDDLE = list(set(ALL_DIGIT) - set(MATCH_MIDDLE))


def test_180_value(test_value):
    test_value_list = map(int, str(test_value))

    try:
        while len(test_value_list) > 0:
            # Test the value in the middle of the number (only 0, 1 and 8 match)
            if len(test_value_list) == 1:
                if test_value_list[0] in MATCH_MIDDLE:
                    test_value_list.pop()
                    continue
                else:
                    raise Exception('Do not match middle value')
            # Test the value in the sides of the number
            else:
                if MATCH_SIDE[test_value_list[0]] == test_value_list[-1]:
                    test_value_list.pop()
                    test_value_list.pop(0)
                else:
                    raise Exception('Do not match side value')

        return True
    except:
        return False


assert(test_180_value(180) is False)
assert(test_180_value(69) is True)
assert(test_180_value(916) is True)
assert(test_180_value(11111) is True)
assert(test_180_value(8181818) is True)

# Monkey testing
for i in range(100):
    number_list = []
    number_len = random.randint(1, 10)
    print "Genarate a number of %d size" % number_len

    # if len is odd, insert a correct middle value
    if number_len % 2 == 1:
        number_list.append(random.choice(MATCH_MIDDLE))
        number_len -= 1

    # Then generate the extra parameters
    for k in range(number_len / 2):
        if k == (number_len / 2) - 1:
            left = random.choice(MATCH_EXTREMITY)
        else:
            left = random.choice(MATCH_SIDE.keys())
        right = MATCH_SIDE[left]
        number_list.append(right)
        number_list.insert(0, left)

    good_number = int(''.join(map(str, number_list)))

    print "### GOOD NUMBER %d" % good_number
    assert(test_180_value(good_number) is True)

    # Insert a bad parameter anywhere
    bad_list = list(number_list)
    bad_list.insert(random.randint(0, len(number_list) / 2), random.choice(BAD_SIDE))
    bad_number = int(''.join(map(str, bad_list)))

    print "### BAD NUMBER %d" % bad_number
    assert(test_180_value(bad_number) is False)

    bad_list = list(number_list)
    if len(bad_list) % 2 == 1:
        bad_list[len(bad_list) / 2] = random.choice(BAD_MIDDLE)
    else:
        bad_list.insert(random.randint(0, len(bad_list) / 2), random.choice(BAD_SIDE))
    bad_number = int(''.join(map(str, bad_list)))

    print "### BAD NUMBER %d" % bad_number
    assert(test_180_value(bad_number) is False)
