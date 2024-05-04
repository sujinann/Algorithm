l, n = map(int, input().split())

words = []
for i in range(n):
    words.append(input())

words.sort()

def check(square):
    c = ""
    for i in range(len(square)):
        c += square[i][len(square)]

    return c

def dfs(visited, square):
    if len(square) == l:
        for i in range(l):
            print(square[i])

        exit()
    
    c = check(square)

    for i in range(n):
        if not visited[i]:
            if words[i][:len(square)] == c:
                visited[i] = True
                square.append(words[i])
                dfs(visited, square)
                visited[i] = False
                square.pop()

visited = [False] * n
square = []
dfs(visited, square)
print("NONE")