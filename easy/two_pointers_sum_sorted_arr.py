'''
Find if there are 2 elements in a sorted array which sums up to X
'''

def search(arr: list, x: int) -> bool:
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] + arr[right] == x:
            print(arr[left], arr[right], arr[left] + arr[right])
            return True
        elif arr[left] + arr[right] > x:
            right -= 1
        else:
            left += 1
            
    return False


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 19
    print(search(arr, x))
    print(ord('O'))