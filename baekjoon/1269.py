import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a, b = set(a), set(b)
c, d = (a - b), (b - a)
print(len(c)+len(d))