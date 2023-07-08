'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''


def check(t: tuple, l: list) -> tuple:
    l.pop(t[0])
    lockup = set()
    for num in l:
        if num in lockup:
            return tuple(sorted([-t[1], num, t[1]-num]))
        lockup.add(t[1]-num)


def find_triplets(l: list) -> 'list[list]':
    d1 = {}
    score = []
    for index, num in enumerate(l):
        d1[index] = -num
    for t in d1.items():
        sum_2_check = check(t, l.copy())
        if sum_2_check is not None:
            score.append(sum_2_check)
    return [list(x) for x in set(score)]


if __name__ == '__main__':
    print(find_triplets([-1,0,1,2,-1,-4]))
