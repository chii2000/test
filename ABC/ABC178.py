
"""
#A
a = input()
if int(a) == 1:
    print(0)
else:
    print(1)
"""

#B
"""
a, b, c, d = map(int, input().split())
e = []
for i in range(a, b + 1):
    for j in range(c, d + 1):
        e += [i * j]
print(max(e))
"""
"""
a, b, c, d = map(int, input().split())
if b > 0 and d > 0:
    print(b * d)
elif b > 0 and d < 0:
    print(a * d)
elif b < 0 and d > 0:
    print(b * c)
elif b <= 0 and d <= 0:
    print(a * c)
"""
"""
a, b, c, d = map(int, input().split())
e = []
for i in [a, b]:
    for j in [c, d]:
        e += [i * j]

print(max(e))
"""
"""
#178C
N = input()
n = int(N)
print((n * (n - 1) * 10 **(n - 2)) % ((10 ** 9) + 7))
"""
n = int(input())
print((10 ** n - 9 ** n * 2 + 8 ** n) % (10 ** 9 + 7))


    