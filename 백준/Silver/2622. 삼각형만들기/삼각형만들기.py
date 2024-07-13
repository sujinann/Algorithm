n = int(input())

answer = 0
if n == 1 or n == 2 or n == 4:
    answer = 0
else:
    for i in range(1, n):
        for j in range(i, n):
            k = n - i - j
            if j <= k and i + j > k :
                answer += 1

print(answer)