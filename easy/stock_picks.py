'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def calc(l: list) -> int:
    max = 0
    min = float('inf')
    for num in l:
        if min > num:
            min = num
        if num - min > max:
            max = num - min
    return max


print(calc([7,6,4,3,1]))