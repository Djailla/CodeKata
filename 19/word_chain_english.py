#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Working on exercice :

http://codekata.com/kata/kata19-word-chains/
"""

import heapq

INPUT_STR = 'gold'
INPUT_STR_LEN = len(INPUT_STR)
DEST_STR = 'lead'


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def get_close_str(input_str, word_set):
    """Generate a set of word that can be the next step in the word chain"""
    matching_words = set()

    for word in word_set:
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
    count = INPUT_STR_LEN

    for i in range(INPUT_STR_LEN):
        if scr_str[i] == dest_str[i]:
            count -= 1
    return count


def main():
    word_set = set()

    # Basic check
    if INPUT_STR_LEN != len(DEST_STR):
        print 'String %s and %s do not have the same len (%d != %d)' % (
            INPUT_STR, DEST_STR, INPUT_STR_LEN, len(DEST_STR)
        )
        return

    # Copy in memory the list of words with the correct length
    with open('../common/english.txt', 'r') as word_list:
        word_set = set(
            word.lower().strip().replace('\'', '')
            for word in word_list.readlines()
            if len(word.lower().strip().replace('\'', '')) == INPUT_STR_LEN
        )

    # Check if words exists
    if INPUT_STR not in word_set:
        print 'This word do not exists %s' % INPUT_STR
        return

    if DEST_STR not in word_set:
        print 'This word do not exists %s' % DEST_STR
        return

    word_queue = PriorityQueue()
    word_queue.put(INPUT_STR, 0)
    came_from = {}
    cost_so_far = {}
    came_from[INPUT_STR] = None
    cost_so_far[INPUT_STR] = 0

    while not word_queue.empty():
        current = word_queue.get()

        if current == DEST_STR:
            break

        for next in get_close_str(current, word_set):
            # print ">>> %s" % next

            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + get_score(next, DEST_STR)
                word_queue.put(next, priority)
                came_from[next] = current

    current = DEST_STR
    path = [current]
    while current != INPUT_STR:
        current = came_from[current]
        path.append(current)
    path.reverse()

    print '\n'.join(path)

if __name__ == "__main__":
    main()
