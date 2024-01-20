'''
given a string and a word, find all the occurences of the word anagrams and return the starting indexes
'''

from collections import Counter


def search(s: str, word: str):
    word_char_count = Counter(word)
    window_len = len(word)
    index_list = []
    
    for i in range(len(s)-window_len+1):
        if Counter(s[i:i+window_len]) == word_char_count:
            index_list.append(i)

    return index_list    
    
if __name__ == '__main__':
    res = search(s='babca', word='aabc')
    print(res)
