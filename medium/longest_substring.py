
'''Given a string s, find the length of the longest 
substring
 without repeating characters.'''
 
def search(s: str) -> str:
    found_chars = set()
    left = right = temp_sub_len = 0
    while right < len(s):
        if s[right] not in found_chars:
            found_chars.add(s[right])
            if len(s[left: right]) > temp_sub_len:
                temp_sub_len = len(s[left: right])
            right += 1
        else:
            found_chars = set()
            left += 1
            right = left+1
            
    return temp_sub_len


if __name__ == '__main__':
    s = "pwwkew"
    print(search(s))