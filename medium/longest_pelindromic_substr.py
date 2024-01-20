'''
Given a string s, return the longest 
palindromic substring in s
'''


def find(s: str) -> str:
    left = right = count = 0
    for i in range(len(s)):
        for j in range(len(s) - 1, i ,-1):
            if is_palindrome(s[i:j]):
                if j - i > count:
                    count = j - i
                    left, right = i, j

    return s[left:right+1]                  


def is_palindrome(s: str) -> bool:
    # recursive solution just for fun
    if len(s) == 1:
        return True
    if len(s) == 2 and s[0] == s[1]:
        return True
    if len(s) == 3 and s[0] == s[2]:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


# dynamic programming approach suggested by ChatGPT - O(n^2)
# much faster than the recursive approach 
def find2(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    start = max_len = 0
    dp = [[False] * n for _ in range(n)]

    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check for palindromes of length > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    for row in dp:
        print(row)

    return s[start:start + max_len]

if __name__ == '__main__':
    print(find2("abba"))
