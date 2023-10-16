import sys
input = sys.stdin.readline
n = int(input())
h = list(map(int, input().split()))
m = int(input())
g = list(map(int, input().split()))
dic = {}
for i in range(len(h)):
    dic[h[i]] = 1
for i in range(len(g)):
    if g[i] in dic:
        print(dic[g[i]], end=' ')
    else:
        print(0, end=' ')