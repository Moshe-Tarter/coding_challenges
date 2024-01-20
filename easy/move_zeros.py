'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array
'''

def moveZeroes(nums):
    non_zero_index = 0  # Initialize the non_zero_index to 0
    
    # Iterate through the array
    for current in range(len(nums)):
        if nums[current] != 0:
            print(nums)
            # Swap the non-zero element with the element at non_zero_index
            nums[current], nums[non_zero_index] = nums[non_zero_index], nums[current]
            non_zero_index += 1  # Increment the non_zero_index
    
    return nums

if __name__ == '__main__':
    nums = [0, 1, 0, 2, 3]
    moveZeroes(nums)
    print(nums)