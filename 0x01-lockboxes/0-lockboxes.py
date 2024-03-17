#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    visited = set()
    queue = [0]  # Start from the first box

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                queue.append(key)
                visited.add(key)  # Add the key to visited

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

# Testing the function
print(canUnlockAll([[1], [2], [3], [4], []]))  # True
print(canUnlockAll([[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]))  # True
print(canUnlockAll([[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]))  # False
print(canUnlockAll([[0]])) # True
