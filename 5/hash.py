#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata05-bloom-filters/
"""

class HastTable:
    def __init__(self):
        self.size = 50000
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            next_slot = self.slots[rehash(hashvalue)]
            while self.slots[next_slot] is not None:
                next_slot = self.slots[rehash(hashvalue)]

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data

        return

    def hashfunction(self, key):
        return

    def rehash(self, oldhash):
        return (oldhash+1) % self.size

    def get(self, key):
        return
