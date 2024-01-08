import sys
input = sys.stdin.readline

sudoku = []
for i in range(9):
    sudoku.append(list(map(int, input().split())))

def col(r, c):
    check = 0
    for i in range(9):
        if i != c and sudoku[r][i] == sudoku[r][c]:
            check = 1
            break
    if check == 0:
        return True
    else:
        return False
        
def row(r, c):
    check = 0
    for i in range(9):
        if i != r and sudoku[i][c] == sudoku[r][c]:
            check = 1
            break
    if check == 0:
        return True
    else:
        return False

def square(r, c):
    check = 0
    for i in range((r//3)*3, (r//3)*3+3):
        for j in range((c//3)*3, (c//3)*3+3):
            if i == r and j == c:
                continue
            if sudoku[r][c] == sudoku[i][j]:
                check = 1
                break
    if check == 0:
        return True
    else:
        return False
    
answer = False

    
def dfs(r, c, p):
    global answer

    if answer:
        return

    if p == 0:
        answer = [s[:] for s in sudoku]
        return
    
    r = blank[cnt-p][0]
    c = blank[cnt-p][1]
    for k in range(1, 10):
        sudoku[r][c] = k
        if col(r, c) and row(r, c) and square(r, c):
            dfs(r, c, p-1)
        sudoku[r][c] = 0

blank = []
cnt = 0
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            cnt += 1
            blank.append([i, j])

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            dfs(i, j, cnt)

for i in range(9):
    print(*answer[i])
