import sys
input = sys.stdin.readline
t = int(input())
p = list(map(int, input().split()))
if len(p)%2 == 0:
    result = min(p)*max(p)
else:
    result = sorted(p)[t//2]**2
print(result)