n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

answer = 0
for i in range(len(a)):
    answer += a[i] * b[len(a)-i-1]

print(answer)