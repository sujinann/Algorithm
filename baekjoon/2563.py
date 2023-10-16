N = int(input())
arr = []
result = 0
for i in range(100):
    arr.append([0]*100)

for i in range(N):
    x, y = (map(int, input().split()))
    for j in range(x-1, x+9):
        for p in range(y-1, y+9):
            arr[j][p] = 1

for i in range(100):
    result += arr[i].count(1)

print(result)