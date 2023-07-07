import typing

'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

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