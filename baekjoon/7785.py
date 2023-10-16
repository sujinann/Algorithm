import sys
input = sys.stdin.readline
n = int(input())
ans = {}
for i in range(n):
    a, b = (map(str, input().split()))
    if b == 'enter':
        ans[a] = 1
    else :
        del ans[a]
ans = sorted(ans)
ans.reverse()
print(*ans, sep='\n')