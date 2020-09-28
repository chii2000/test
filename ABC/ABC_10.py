
#86A
a, b = map(int, input().split())
print('Even' if a*b % 2 == 0 else 'Odd')

a, b, c = map(int, input().split())
def marble(a, b, c):
    if a == 1



#81A
s = input()
print(s.count(1))

#81B
N = input()
A = list(map(int, input().split()))
count = 0
while all(a % 2 == 0 for a in A):
    A = [a/2 for a in A]
    count += 1
print(count)


#87B
A, B, C, X = [int(input()) for i in range(4)]
count = 0
for j in range(A + 1):
    for k in range(B + 1):
        for l in range(C + 1):
            if 500 * j + 100 * k +50 * l == X:
                count += 1

print(count)

#83B
n, a, b = map(int, input().split())
count = 0
for i in range(n + 1):
    if a <= sum(list(map(int, str(i))) <= b:
        count += i

print(count)


#83B
N, A, B = map(int, input().split())
for i in range(1, N + 1):
    if A <= sum(map(int, str(i))) <= B:
        print(sum(i))

#88B X
N = int(input())
L1 = list(map(int, input().split()))
L2 = sorted(L1)[::-1]
Alice = []
Bob = []
for i in L2:
    Alice += i
    L2.remove(i)
    for j in L2:
        Bob += j
        L2.remove(j)
print(sum(Alice) - sum(Bob))

#88B
N = int(input())
a = sorted(list(map(int, input().split())))[::-1]
print(sum((a[::2]) - sum(a[1::2])))

#85B
N = int(input())
L = [int(input()) for i in range(N)]
L2 = set(L)
print(len(L2))

#85C X for文の中のifの位置、 
N, Y = map(int, input().split())
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            if 10000*i + 5000*j + 1000*k == Y:
                print(i, j, k)
print('-1, -1, -1')

#85C
N, Y = map(int, input().split())
for i in range(N+1):
    for j in range(N+1-i):
        k = N-i-j
        if 0 <= k <= 2000 and 10000*i + 5000*j + 1000*k == Y:
            print(i, j ,k)
            exit()  #
print('-1, -1, -1')

#49C X
#86C X
N = int(input())
line = [list(map(int, input().split())) for i in range(N)]
for j in line[0][0]:
    for k in (line[0][0]-j):
        if line[0][1] == 1*j + (-1)*k: #さらにfor?
            if line[0][2] == 
                for l in line[1][0]

N = int(input())
line = [list(map(int, input().split())) for i in range(N)]

for i in range(N + 1):
    a = line[i+1][0] - line[i][0]
    b = line[i + 1][1] + line[i + 1][2]
    c = line[i][1] + line[i][2]

if a % 2 == (b - c) % 2:
    print('Yes')
else:
    print('No')


