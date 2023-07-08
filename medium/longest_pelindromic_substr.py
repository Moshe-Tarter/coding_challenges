'''
Given a string s, return the longest 
palindromic substring in s
'''


def find(s: str) -> str:
    left = right = count = temp_count = 0
    for i in range(len(s)):
        for j in range(len(s) - 1, i ,-1):
            if temp_count == 0 and s[i] == s[j]:
                count += 1
                left, right = i, j
            elif s[i] == s[j]:
                count += 1
            else:
                if temp_count > count:
                    left, right = i, j
                temp_count = 0

    return s[left:right+1]                  


if __name__ == '__main__':
    print(find("cbbd"))
