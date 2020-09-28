"""
x =[0, 1, 2, 3, 4, 5]
for i in range(5):
    print(x[i])
y = [1, 3, 4]
for v in y:
    print(v)
z = [[1, 2, 3], [4, 5, 6]]
for c in z:
    for d in c:
        print(d)

for n in range(2):
    for m in range(3):
        print(z[n][m])
"""


def t(a, b):
    c = a * b
    if c // 2 == 0:
        print("偶数")
    else:
        print("奇数")

a = 49
b = 25
print(t(a,b))


a, b = map(int, input().split())
if (a*b) % 2 == 0:
    print('Odd')
else:
    print('Even')







