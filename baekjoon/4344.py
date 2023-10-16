C = int(input())
for i in range(C):
    sum = 0
    cnt = 0
    L = []
    S = list(map(int, input().split()))
    for i in S[1: S[0] + 1]:
        L.append(i)
    for i in L :
        sum += i
    A = sum / S[0] 
    for i in L :
        if i > A :
            cnt += 1
    print("%.3f%%" %((cnt / S[0])*100))

