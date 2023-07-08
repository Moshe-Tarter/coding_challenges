'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

def pad(l1: list, l2: list) -> list:
    if len(l1) > len(l2):
        return l1, [0]*(len(l1) - len(l2)) + l2
    elif len(l1) < len(l2):
        return l2, [0]*(len(l2) - len(l1)) + l1
    return l1, l2
    


def sum_lists(l1: list, l2: list) -> int:
    carry = 0
    res = []
    l1, l2 = pad(l1, l2) 
    for x, y in zip(reversed(l1), reversed(l2)):
        temp_sum = x + y + carry
        carry = 0
        if temp_sum > 9:
            res.append(temp_sum % 10)
            carry += 1
        else:
            res.append(temp_sum)
    return res


if __name__ == '__main__':
    print(sum_lists(l1 = [2,4,3], l2 = [5,6,4]))
