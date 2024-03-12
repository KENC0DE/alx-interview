#!/usr/bin/python3
"""
LockBoxes
"""


def canUnlockAll(boxes):
    """Try to Unlock"""
    if not boxes or boxes == []:
        return False
    def opener(boxes, keys, key):
        """Recursion Unlock"""
        if key in keys or key >= len(boxes):
            return
        if boxes[key] == []:
            keys.append(key)
            return
        keys.append(key)
        for i in range(len(boxes[key])):
            opener(boxes, keys, boxes[key][i])

    keys = []
    key = 0
    opener(boxes, keys, key)
    return len(boxes) == len(keys)
