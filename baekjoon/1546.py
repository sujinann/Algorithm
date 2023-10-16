N = int(input())
score = list(map(int, input().split()))
M = max(score)
x = 0

for i in score:
    x += i

print(((x/M)/3)*100)