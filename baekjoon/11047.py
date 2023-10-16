N, K = map(int, input().split())
arr = []
x = 0
for i in range(1, N + 1) :
    arr.append(int(input()))

arr.reverse()
for a in arr :
    if a <= K :


x += (K // a) 
