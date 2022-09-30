from extratypes import Tree  # library with types used in the task


def solution(T):
    return calculate_depth(T, -1)


def calculate_depth(node, depth):
    if not node:
        return depth

    return max(calculate_depth(node.l, depth + 1), calculate_depth(node.r, depth + 1))
