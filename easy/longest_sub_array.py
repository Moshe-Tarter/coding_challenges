import typing

'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
'''

def find(arr: list) -> int:
    global_max = 0
    temp = 0

    for num in arr:
        temp = temp + num
        if temp > global_max:
            global_max = temp
        if temp < 0:
            temp = 0

    return global_max


if __name__ == '__main__':
    print(find([5,4,-1,7,8]))