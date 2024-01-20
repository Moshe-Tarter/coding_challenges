'''
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
'''

def search(s: str, words: list) -> list:
    
    return_list = []
    word_len = len(words[0])
    temp_set = set()
    index = 0
    temp_index = 0
    while index < len(s):
        print(index, s[index: index+word_len])
        if s[index: index+word_len] in words and s[index: index+word_len] not in temp_set:
            if len(temp_set) == 0:
                temp_index = index
            temp_set.add(s[index: index+word_len])
            
            if temp_set == set(words):
                return_list.append(temp_index)
                index += 1
                temp_set = set()
            else:
                index += word_len
                
        elif s[index: index+word_len] in words and s[index: index+word_len] in temp_set:
            temp_set = set()
            temp_set.add(s[index: index+word_len])
            temp_index = index
            index += word_len
            
        else:
            temp_set = set()
            index += 1
        
    return return_list


if __name__ == '__main__':
    s = 'abcdefxdxcababcdeffabcdabcabcdefff'
    words = ['fxx', 'cab']
    print(search(s, words))
            