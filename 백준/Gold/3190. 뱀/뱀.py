from collections import deque


n = int(input())
k = int(input())

apples = []
visited = []
for i in range(k):
    apple = list(map(int, input().split()))
    apples.append(apple)

l = int(input())
commands = []
for i in range(l):
    time, direct = input().split()
    time = int(time)
    commands.append([time, direct])

snake = deque([[1, 1]])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direct = 1
answer = 0
flag = False

for c in commands:
    t = c[0]
    d = c[1]

    for second in range(t-answer):
        answer += 1

        x = snake[-1][0]
        y = snake[-1][1]

        nx = x + dx[direct]
        ny = y + dy[direct]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            flag = True
            break

        if [nx, ny] in snake:
            flag = True
            break

        snake.append([nx, ny])

        if [nx, ny] not in apples:
            snake.popleft()
        else:
            if [nx, ny] in visited:
                snake.popleft()
            else:
                visited.append([nx, ny])

    if flag:
        break
    
    if d == 'L':
        dir = -1
    else:
        dir = 1

    direct = (4 + (direct + dir)) % 4


if not flag:
    while True:
        answer += 1

        x = snake[-1][0]
        y = snake[-1][1]

        nx = x + dx[direct]
        ny = y + dy[direct]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            flag = True
            break

        if [nx, ny] in snake:
            flag = True
            break

        snake.append([nx, ny])

        if [nx, ny] not in apples:
            snake.popleft()
        else:
            if [nx, ny] in visited:
                snake.popleft()
            else:
                visited.append([nx, ny])

print(answer)