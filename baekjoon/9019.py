from collections import deque


def dd(temp):
    newtemp = (temp * 2) % 10000
    return newtemp

def ss(temp):
    newtemp = temp - 1
    if newtemp == -1:
        newtemp = 9999
    return newtemp

def left(temp):
    a = temp // 1000
    b = (temp // 100) % 10
    c = (temp // 10) % 10
    d = temp % 10

    newtemp = b * 1000 + c*100 + d*10 + a
    return newtemp

def right(temp):
    a = temp // 1000
    b = (temp // 100) % 10
    c = (temp // 10) % 10
    d = temp % 10

    newtemp = d * 1000 + a*100 + b*10 + c
    return newtemp


T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())

    answer = ""
    visited = [False]*10000
    
    q = deque()
    q.append([A, answer])
    visited[A] = True

    while q:
        tt, answer = q.popleft()
        if tt == B:
            break

        ttt = dd(tt)
        if not visited[ttt]:        
            visited[ttt] = True
            q.append([ttt, answer + "D"])
        
        ttt = ss(tt)
        if not visited[ttt]:        
            visited[ttt] = True                
            q.append([ttt, answer + "S"])

        ttt = left(tt)
        if not visited[ttt]:        
            visited[ttt] = True
            q.append([ttt, answer + "L"])

        ttt = right(tt)
        if not visited[ttt]:        
            visited[ttt] = True
            q.append([ttt, answer + "R"])


    print(answer)