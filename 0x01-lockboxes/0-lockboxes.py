#!/usr/bin/python3
"""
LockBoxes
"""


def canUnlockAll(boxes):
    """Try to Unlock"""
    def opener(boxes, keys, key):
        """Recursion Unlock"""
        if key in keys:
            return
        if boxes[key] == []:
            keys.append(key)
            return
        keys.append(key)
        for i in range(len(boxes[key])):
            opener(boxes, keys, boxes[key][i])

    keys = [-1,]
    key = 0
    opener(boxes, keys, key)
    keys = keys[1:]
    return len(boxes) == len(keys)
