import sys
input = sys.stdin.readline
l = []
n = int(input())
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort(key = lambda x : (x[1], x[0]))
for i in l:
    print(i[0], i[1])