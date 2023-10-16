n = int(input())
board = []
for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)

answer = 0

def move(temp_board):
    new_board = [[0] * n for i in range(n)]

    for i in range(n):
        target = -1
        new = []
        for j in range(n):
            if temp_board[j][i] != 0:
                if target == -1:
                    target = temp_board[j][i]

                else:
                    if temp_board[j][i] == target:
                        new.append(target*2)
                        target = -1
                        continue
                    else:
                        new.append(target)
                        target = temp_board[j][i]
            
            if j == n-1 and target != -1:
                new.append(target)
                    
        for k in range(len(new)):
            new_board[k][i] = new[k]

    return new_board

def turn(temp_board, k):
    if k == 0:
        return temp_board
    
    if k == 1:
        new_board = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                new_board[n-1-j][i] = temp_board[i][j]

        return new_board

    if k == 3:
        new_board = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                new_board[j][n-1-i] = temp_board[i][j]

        return new_board

    if k == 2:
        new_board = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                new_board[n-1-i][j] = temp_board[i][j]

        return new_board
    
    if k == 4:
        return temp_board

def dfs(temp_board, cnt):
    global answer
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if temp_board[i][j] > answer:
                    answer = temp_board[i][j]

        return
    
    for i in range(4):

        dfs(turn(move(turn(temp_board, i)),4-i), cnt+1)
        
dfs(board, 0)
print(answer)