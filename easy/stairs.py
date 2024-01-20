'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

def stairs_it(n: int) -> int:
    arr = []
    arr.append(1)
    arr.append(1)
    for x in range(n):
        arr.append(arr[x] + arr[x+1])
    return arr[n]


def stairs_rec(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return stairs_rec(n-2) + stairs_rec(n-1)


if __name__ == '__main__':
    print(stairs_rec(40))