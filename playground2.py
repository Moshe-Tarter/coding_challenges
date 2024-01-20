# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# #2sum
# def find(arr: list, target: int) -> list:
#     lookup_set = dict()
#     index_list = list()
#     for index, number in enumerate(arr):
#         if target-number in lookup_set.keys():
#             index_list.append(index)
#             index_list.append(lookup_set.get(target-number))
#             break
#         else:
#             lookup_set[number] = index

#     return index_list


# #add 2 numbers
# def add2numbers(num1: ListNode, num2: ListNode) -> ListNode:
#     carry = 0
#     head = ListNode()
#     current = head
#     while num1 or num2 or carry:
#         value1 = num1.val if num1 else 0
#         value2 = num2.val if num2 else 0
        
#         temp_sum = value1 + value2 + carry
#         carry, temp_val = divmod(temp_sum, 10)
        
#         current.next = ListNode(val=temp_val)
#         current = current.next
        
#         if num1:
#             num1 = num1.next
#         if num2:
#             num2 = num2.next
            
#     return head.next
            
# if __name__ == '__main__':
#     num1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))))))
#     num2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))
#     res = add2numbers(num1, num2)
#     while res:
#         print(res.val)
#         res = res.next
#     divmod

# import threading


# def print_cube(num):
# 	print("Cube: {}" .format(num * num * num))


# def print_square(num):
# 	print("Square: {}" .format(num * num))


# if __name__ =="__main__":
# 	t1 = threading.Thread(target=print_square, args=(10,))
# 	t2 = threading.Thread(target=print_cube, args=(10,))

# 	t1.start()
# 	t2.start()

# 	t1.join()
# 	t2.join()

# 	print("Done!")

from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import os


def timeit(fn):
    from time import perf_counter as c
    
    def inner(*args, **kwargs):
        start = c()
        fn()
        print(c()-start)
        
    return inner


def square(x):
    #print(os.getpid())
    return x * x

@timeit
def ex():
    with ThreadPoolExecutor() as executor:
        return list(executor.map(square, data))
    
    
@timeit
def ex_mp():
    with Pool() as pool:
        return pool.map(square, data)

if __name__ == "__main__":
    data = range(1000000)
    #ex()
    ex_mp()
