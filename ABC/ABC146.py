#A
s = input()
S = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(7-S.index(s))

#B
import string
n = int(input())
s = input()

l = string.ascii_uppercase
ans = [l[(l.index(i) + n ) % len(l)] for i in s]
print(''.join(ans))

#C
a, b, x = map(int, input().split())
def is_ok(arg):
    return a*arg + b*len(str(arg)) <= x

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(10*9 + 1, 0))