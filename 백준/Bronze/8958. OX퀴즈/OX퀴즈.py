t = int(input())
for tc in range(t):
    s = input()
    answer = 0
    cnt = 0
    for i in s:
        if i == "O":
            cnt += 1
        else:
            cnt = 0
        answer += cnt
    print(answer)