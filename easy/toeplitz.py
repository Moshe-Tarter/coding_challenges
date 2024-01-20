'''
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.
'''

def check(m: list[list]) -> bool:
    rows_count = len(m)
    row_len = len(m[0])
    # iterate first row
    for pos in range(len(m[0])-1):
        print(pos)
        print('-'*20)
        temp_pos = pos
        row = 0
        while True:
            print(f'pos is {row, temp_pos}')
            if row + 1 < rows_count and pos+1 < row_len:
                if m[row][temp_pos] != m[row+1][temp_pos+1]:
                    return False
                else: 
                    row = row + 1
                    temp_pos += 1
            else:
                print('...')
                break
    
    #iterate first col
    col = 0
    for pos in range(1, rows_count-1):
        while True:
            if col + 1 < row_len and pos + 1 < rows_count:
                if m[pos][col] != m[pos+1][col+1]:
                    return False
                else:
                    col = col + 1
                    break
            else:
                break 
    
    return True
            

if __name__ == '__main__':
    arr = [ 
            [1, 2, 3, 4, 83],
            [5, 1, 2, 3, 4],
            [4, 5, 1, 2, 3],
            [7, 4, 5, 1, 2]
        ]
    
    print(check(arr))