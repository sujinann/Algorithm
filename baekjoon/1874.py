import sys
input = sys.stdin.readline
n = int(input())
stack = []
cnt = 0
result = []
for i in range(n):
    s = int(input())
    if s not in stack:
        for j in range(cnt, s):
            stack.append(j+1)
            result.append('+')
            cnt += 1
        result.append('-')
        stack.pop()
    elif s in stack and s == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        result = 'NO'
        break
if result == 'NO':
    print(result)
else:
    for i in result:
        print(i)