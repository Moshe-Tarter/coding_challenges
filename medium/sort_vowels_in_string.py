'''
Given a 0-indexed string s, permute s to get a new string t such that:

All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
'''

vowels = ['a', 'i', 'e', 'o', 'u', 'A', 'I', 'E', 'O', 'U']

def sort_vowels(s: str) -> str:
    l = list(s)
    for j in range(len(l)):
        for k in range(len(l) - j):
            if j != k:
                if l[j] in vowels and l[k] in vowels:
                    if ord(l[j]) < ord(l[k]):
                        l[j], l[k] = l[k], l[j]
    return ''.join(l)


if __name__ == '__main__':
    s = 'lYmpH'
    print(sort_vowels(s))