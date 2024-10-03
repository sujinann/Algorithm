x, y = map(int, input().split())

d = y - x
temp = int(d ** (1/2)) - 1

answer = 0
for i in range(3):
    t = temp + i

    if t * (t+1) < d <= (t+1) ** 2 :
        answer = 2 * t + 1
        break
    elif (t+1) ** 2 < d <= (t+1) * (t+2):
        answer = 2 * t + 2
        break

print(answer)