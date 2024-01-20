# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
# def merge(l1, l2):
#     new = ListNode()
#     current = new
#     while l1 and l2:
#         if l1.val < l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next
    
#     if l1:
#         current.next = l1
#     else:
#         current.next = l2
        
#     return new.next

def rotate(head):
    current = head
    
    prev = None
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def get_mid_node(head):
    if head is None or head.next is None:
        return True
    
    middle, end = head, head
    while end and end.next:
        middle = middle.next
        end = end.next.next
        
    print(middle.val)
    print(middle.next.val)
        
    return middle

def check_pal(head1):
    head2 = get_mid_node(head1)
    tail = rotate(head2)
    print(tail.val)
    print(head1.val)
    while head1.next is not None:
        if head1.val != tail.val:
            print(head1.val, tail.val)
            return False
        head1 = head1.next
        tail = tail.next
        
    return True


if __name__ == '__main__':
    # l1 = ListNode(1, next=ListNode(5, next=ListNode(4, next=ListNode(3, ListNode(1)))))
    # l2 = ListNode(2, next=ListNode(5, next=ListNode(7, next=ListNode(91))))
    # # while l1:
    # #     print(l1.val)
    # #     l1 = l1.next
    # # l1 = ListNode(1, next=ListNode(3, next=ListNode(6, next=ListNode(8))))
    # # out = rotate(l1)
    # # merged_list = merge(l1, l2)
    # # while out:
    # #     print(out.val)
    # #     out = out.next
    
    # print(check_pal(l1))
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://localhost:3007/authors/books/'
    #params = {'api-key': 'XUP5kGd7sQbkfGtQFtS1mAkiH67CjeVE'}
    
    data = requests.get(url=url, params={'author': 'Stephen King'})
    # reviews = data.json().get('results')
    # books = set()
    # for review in reviews:
    #     books.add(review.get('book_title'))
        
    # print(books)
    
    # def get_author_reviews():
    #     pass
    
    # def extract_book_names_from_reviews():
    #     pass response.json().get('results')
    #data = data.json()
    print(type(data.text))
    print(data.json)
    soup = BeautifulSoup(data.text, 'html.parser')

    # print(data.status_code)
    # print(data.url)
    # print(data.headers)
    # Find all <p> elements in the HTML
    paragraph_elements = soup.find_all('p')

    # Extract and print the text from each <p> element
    for paragraph in paragraph_elements:
        print(paragraph.text)