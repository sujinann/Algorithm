t = int(input())

for tc in range(t):
    startx, starty, targetx, targety = map(int, input().split())
    n = int(input())
    answer = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        f = (startx - cx) ** 2 + (starty - cy) ** 2
        g = (targetx - cx) ** 2 + (targety - cy) ** 2
        cnt = 0
        if f <= r**2:
            cnt += 1
        if g <= r**2:
            cnt += 1

        if cnt == 1:
            answer += 1

    print(answer)