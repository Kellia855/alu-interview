#!/usr/bin/python3
"""
rain module
Contains the rain(walls) function that calculates
how much rainwater can be retained between walls.
"""

def rain(walls):
    """
    Calculate how many square units of water will be retained.

    Args:
        walls (list): List of non-negative integers.

    Returns:
        int: Total amount of retained rainwater.
    """
    if not walls or len(walls) < 3:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, walls[left])
            water += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            water += right_max - walls[right]

    return water
