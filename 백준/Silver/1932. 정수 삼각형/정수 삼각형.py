n = int(input())

triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(n-1):
    for j in range(n-1-i):
        triangle[n-2-i][j] += max(triangle[n-1-i][j], triangle[n-1-i][j+1])

answer = triangle[0][0]
print(answer)