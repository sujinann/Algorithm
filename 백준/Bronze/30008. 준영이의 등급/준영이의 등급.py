n, k = map(int, input().split())
l = list(map(int, input().split()))

answer = []
for i in l:
    if 0 <= i*100//n <= 4:
        answer.append(1)
    elif 4 < i*100//n <= 11:
        answer.append(2)
    elif 11 < i*100//n <= 23:
        answer.append(3)
    elif 23 < i*100//n <= 40:
        answer.append(4)
    elif 40 < i*100//n <= 60:
        answer.append(5)
    elif 60 < i*100//n <= 77:
        answer.append(6)
    elif 77 < i*100//n <= 89:
        answer.append(7)
    elif 89 < i*100//n <= 96:
        answer.append(8)
    elif 96 < i*100//n <= 100:
        answer.append(9)

print(*answer)