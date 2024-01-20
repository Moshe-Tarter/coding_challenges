
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    from collections import Counter

    nums_dict = Counter(nums)
    print(id(nums))
    nums.clear()
    nums.append([0]*nums_dict[0] + [1]*nums_dict[1] + [2]*nums_dict[2])
    print(id(nums))
    return nums
    
if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    print(sortColors(nums))