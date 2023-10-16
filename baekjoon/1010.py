import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s, a = 1, 1
    for i in range(n):
        s *= m-i
    for i in range(n):
        a *= n-i
    print(s//a)