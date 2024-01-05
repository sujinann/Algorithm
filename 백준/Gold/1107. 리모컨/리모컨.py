n = int(input())
m = int(input())
if m == 0:
    b = []
else:
    b = list(map(int, input().split()))

answer = abs(n-100)

if answer != 0:
    for i in range(1000001):
        s = str(i)
        for j in range(len(s)):
            if int(s[j]) in b:
                break
            if j == len(s)-1:
                answer = min(answer, abs(i-n)+len(str(i)))
        if answer == 0:
            break

print(answer)