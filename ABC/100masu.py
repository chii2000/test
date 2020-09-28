
from bisect import bisect_right
import sys
read = sys.stdin.readline

n, k = list(map(int, read().split()))
a = list(map(int, read().split()))
b = list(map(int, read().split()))
a.sort()
b.sort()

def is_ok(x):
    cnt = 0
    for i in a:
        aa = x // i
        cnt += bisect_right(b, aa)
        return cnt >= k

def meguru_bisect(ng, ok):
    while (abs(ok-ng) > 1):
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(-1, 10 ** 18 + 1))


