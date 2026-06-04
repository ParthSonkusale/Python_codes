from math import comb

def height(n, m):
    Add = 0

    for i in range(1, n + 1):
        Add += comb(m, i)

    return Add