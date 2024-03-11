#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes or len(boxes) == 1:
        return True

    visited = [False] * len(boxes)
    visited[0] = True

    keys = [0]

    while keys:
        current_key = keys.pop()
        current_box = boxes[current_key]

        for key in current_box:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                keys.append(key)

    return all(visited)
