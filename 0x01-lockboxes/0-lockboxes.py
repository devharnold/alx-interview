#!/usr/bin/python3
from typing import List
from collections import Queue, deque

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
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        keys = boxes[current_box]
        for boxes in queue.len(boxes):
            if current_box not in visited:
                visited.add(boxes)
                queue.enqueue(boxes)
        return boxes