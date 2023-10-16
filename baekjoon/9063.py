N = int(input())
W, H = [], []
for i in range(N):
    M = list(map(int, input().split()))
    W.append(M[0])
    H.append(M[1])
print((max(W) - min(W)) * (max(H) - min(H)))