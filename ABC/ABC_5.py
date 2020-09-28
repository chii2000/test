#1
a, b = list(map(int, input().split()))
if a*b % 2 == 0:
    print('Even')
else:
    print('Odd')

#2
l = list(input())
cnt = 0
for i in l:
    if i == '1':
        cnt += 1
print(cnt)

#2.1
s = input()
print(s.count('1'))

#3 X
n = int(input())
l = list(map(int, input().split()))
cnt = 0
while all(i % 2 == 0 for i in l):
    l = [i/2 for i in l]
    cnt += 1
print(cnt)

#6
n = int(input())
a = sorted(list(map(int, input().split())))[::-1]
alice = sum(a[0::2])
bob = sum(a[1::2])
print(alice-bob)

#8
n, y = map(int, input().split())
for i in range(n+1):
    for j in range(n+1-i):
        z = n-i-j
        if 0 <= z <= 2000 and 10000*i+5000*j+1000*z == y:
            print(i, j, z)
            exit()
print('-1, -1, -1')
