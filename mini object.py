import math
def cal(n, m):
    if n < m:
        return 0
    ways = math.comb(m + n - 1, m - 1)
    return ways
if __name__ == '__main__':
    n = 9
    m = 5
    result = cal(n, m)
    print(result)