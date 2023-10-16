k, n = map(int, input().split())
l = []
maxi = 0
for i in range(k):
    a = int(input())
    l.append(a)
    if a > maxi:
        maxi = a

if n%k == 0:
    temp = n//k
else:
    temp = n//k+1

answer = maxi//temp
cnt = 0
while cnt < n:
    answer = maxi // temp
    cnt = 0
    for i in range(k):
        cnt += l[i] // answer
    temp += 1

if n == k:
    answer = min(l)

print(answer)