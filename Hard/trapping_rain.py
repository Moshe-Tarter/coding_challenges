import numpy as np

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
'''


def convert_to_2d(arr: list) -> np.ndarray:
    grid = np.zeros(shape=(max(arr), len(arr)))
    for index, building in enumerate(arr):
        for j in range(building):
            grid[j][index] = 1

    return grid


def check_row(arr: list) -> int:
    count = 0
    for i, x in enumerate(arr):
        if len(arr) -1 > i > 0:
            if 1 in arr[:i] and 1 in arr[i+1:] and x == 0:
                count += 1
    return count


def calculate_rain(arr: list) -> int:
    count = 0
    grid = convert_to_2d(arr)
    for row in grid:
        count += check_row(row)
            
    return count



if __name__ == '__main__':
    print(calculate_rain([4,2,0,3,2,5]))
