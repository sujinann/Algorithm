import sys
input = sys.stdin.readline

n = int(input())
al = set(map(int, input().split()))
m = int(input())
bl = list(map(int, input().split()))

for i in bl:
    if i in al:
        print(1)
    else:
        print(0)