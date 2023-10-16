from collections import deque


N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input())))


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


answer = []

def bfs(maps, r, c):
    global answer
    q = deque()
    maps[r][c] = 0
    q.append([r, c])
    cnt = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            

            if 0<=nr<N and 0<=nc<N and maps[nr][nc] == 1:
                cnt += 1
                maps[nr][nc] = 0
                q.append([nr, nc])

    answer.append(cnt)

for r in range(N):
    for c in range(N):

        if maps[r][c] == 1:
            bfs(maps, r, c)
            

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])

# from collections import deque


# N = int(input())
# maps = []
# for i in range(N):
#     maps.append(list(map(int, input())))


# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]


# answer = []

# for r in range(N):
#     for c in range(N):

#         if maps[r][c] == 1:
            
#             q = deque()
#             maps[r][c] = 0
#             q.append([r, c])
#             cnt2 = 1
            

#             while q:
                
#                 r, c = q.popleft()

#                 for i in range(4):
#                     nr = r + dr[i]
#                     nc = c + dc[i]


#                     if 0<=nr<N and 0<=nc<N and maps[nr][nc] == 1:
#                         cnt2 += 1
#                         maps[nr][nc] = 0
#                         q.append([nr, nc])

#             answer.append(cnt2)

# answer.sort()
# print(len(answer))
# for i in range(len(answer)):
#     print(answer[i])