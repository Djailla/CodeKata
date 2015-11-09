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

MATCH_SIDE = {
    0: 0,
    1: 1,
    6: 9,
    8: 8,
    9: 6,
}

MATCH_MIDDLE = [0, 1, 8]


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


print test_180_value(180)
print test_180_value(69)
print test_180_value(916)
print test_180_value(11111)
print test_180_value(96196)
print test_180_value(8181818)
