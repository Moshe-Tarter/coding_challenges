'''
Given a string s, find the length of the longest 
substring
 without repeating characters.
'''


def longest_substr(s: str) -> int:
    lookup = set()
    start = temp_start = 0
    count = temp_count = 0

    if s == '':
        return 0
    else:
        for i, char in enumerate(s):
            if char not in lookup:
                lookup.add(char)
                temp_count += 1
                if temp_count > count:
                    count = temp_count
                    start = temp_start
            else:
                lookup.clear()
                temp_start = s[temp_start:i].index(char) + 1 + temp_start
                print(temp_start)
                temp_count = 0
                for ch in s[temp_start: i+1]:
                    lookup.add(ch)
                    temp_count += 1

    return len(s[start: start+count])

    
if __name__ == '__main__':
    print(longest_substr('thixq is some sting^%13'))
