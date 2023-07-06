'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

ex 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

ex2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

ex3:
Input: nums = [3,3], target = 6
Output: [0,1]

'''


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lockup = set()
    for num in nums:
        if num in lockup:
            return [num, target-num]
        lockup.add(target-num)

        
if __name__ == '__main__':
    arr = [1, 4, 5, 9, 6, 8, 7] # setup pytest and add unit tests for this one
    target = 8
    print(twoSum(arr, target))
