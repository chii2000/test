#A
S = list(input())
T = list(input())
c = 0
for i in range(3):
    if S[i] == T[i]:
        c += 1
print(c)

#B X1
import math
a, b = map(int, input().split())
print(math.ceil(b/a))

#B X2
a, b = map(int, input().split())
c = 1 #差し込み口の数
cnt = 0 #何個差した
while c-1+a < b:
    c += a-1
    cnt += 1
print(cnt)

#B
a, b = map(int, input().split())
c = 1 #差し込み口の数
cnt = 0 #何個差した
while c < b: #余計な操作はいらん
    c += a-1
    cnt += 1
print(cnt)

#C X
N = int(input())
H = list(map(int, input().split()))
cnt = 0
for i in range(N+1):
    if H[i] > H[i+1]:
        cnt += 1
        exit()   #好きなところに降り立てる
        H.remove(H[i])

#C
N = int(input())
H = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 0 #初期化
ans = max(cnt, ans)
print(ans)

        









