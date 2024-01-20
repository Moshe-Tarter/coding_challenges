'''
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

arr = []
def rev(node: ListNode) -> list:
    if node.next is None:
        pass
    else:
        rev(node.next)
    arr.append(node.val)
    

        
def is_pal(node: ListNode) -> bool:
    while node:
        for num in arr:
            if node.val != num:
                return False
            else:
                node = node.next
    return True


if __name__ == '__main__':
    l = ListNode(5, next=ListNode(8, next=ListNode(3, next=ListNode(4, ListNode(5)))))
    rev(l)
    print(is_pal(l))