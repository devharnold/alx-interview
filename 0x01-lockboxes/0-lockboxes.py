#!/usr/bin/python3

"""
-- n number of locked boxes 
-- each box is numbered from 0 to (n - 1)
-- each box -> keys to other boxes

    --prototype:  
            def canUnlockAll(boxes)
    -- a method that determines if all the boxes can be opened
    -- boxes as a list of lists
    -- a key with the same number of box opens that box
    -- assume all keys += 1
        there can be keys that don't have boxes
    -- the first box(boxes[0]) is unlocked
    -- if boxes can be opened return True, else False
"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited_boxes = set([0])
    unvisited_boxes = set([0]).difference(set([0]))


    while len(unvisited_boxes) > 0:
        boxIdx = unvisited_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in visited_boxes:
            unvisited_boxes = unvisited_boxes.union(boxes[boxIdx])
            visited_boxes.add(boxIdx)
    return n == len(visited_boxes)