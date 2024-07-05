n = int(input())

x = 1
y = 3

answer = 3

for i in range(2, n+1):
    answer = y * 2 + x
    x = y
    y = answer

print(answer % 9901)