import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set()  # set = set() / dict = {} 구분
cnt = 0
for i in range(n):
    s.add(input()) # add = 한개 / update = 여러개 구분
for i in range(m):
    ref = input()
    if ref in s:
        cnt += 1
print(cnt)