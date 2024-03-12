#!/usr/bin/python3
"""
LockBoxes
"""


def canUnlockAll(boxes):
    """Try to Unlock"""
    if len(boxes) <= 1:
        return True
    def opener(boxes, keys, key):
        """Recursion Unlock"""
        if key in keys or key >= len(boxes):
            return
        if boxes[key] == []:
            keys.append(key)
            return
        keys.append(key)
        for i in boxes[key]:
            opener(boxes, keys, i)

    keys = []
    key = 0
    opener(boxes, keys, key)
    return len(boxes) == len(keys)
