square = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]

t = int(input())

for tc in range(t):
    answer = [1, 1, 1]
    l = list(map(int, input().split())) 
    
    for i in range(3):
        for j in range(3):
            if square[l[3]][i] != square[l[j]][i]:
                answer[i] = 0
        
    if sum(answer) == 1:
        print('YES')
    else:
        print('NO')