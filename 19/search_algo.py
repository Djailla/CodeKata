#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Gather algorithm for graph search
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


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


def a_star_algo(clean_word1, len_clean_word1,
                clean_word2, len_clean_word2,
                word_set):
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

    return came_from


def greedy_best_first_algo(clean_word1, len_clean_word1,
                           clean_word2, len_clean_word2,
                           word_set):
    word_queue = PriorityQueue()
    word_queue.put(clean_word1, 0)
    came_from = {}
    came_from[clean_word1] = None

    while not word_queue.empty():
        current = word_queue.get()

        if current == clean_word2:
            break

        for next in get_close_str(current, len_clean_word1, word_set):
            if next not in came_from:
                priority = get_score(next, clean_word2, len_clean_word1)
                word_queue.put(next, priority)
                came_from[next] = current

    return came_from


def dijkstra_algo(clean_word1, len_clean_word1,
                  clean_word2, len_clean_word2,
                  word_set):
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
                priority = new_cost
                word_queue.put(next, priority)
                came_from[next] = current

    return came_from


ALGO_DICT = {
    'astar': a_star_algo,
    'greedy': greedy_best_first_algo,
    'dijkstra': dijkstra_algo
}


def get_path(clean_word1, clean_word2, algo, word_set):

    came_from = ALGO_DICT[algo](
        clean_word1, len(clean_word1),
        clean_word2, len(clean_word2),
        word_set
    )

    current = clean_word2
    path = [current]
    while current != clean_word1:
        if not current in came_from:
            return
        current = came_from[current]
        path.append(current)
    path.reverse()

    return path
