import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    cnt = 0
    result = 0
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    while result < n:    
        for j in range(cnt, len(l)):
            if l[j] == max(l[cnt:]):
                cnt += 1
                result += 1
                if j == m:
                    print(result)
                    break
            else:
                l.append(l[j])
                cnt += 1
                if j == m:
                    m = len(l)-1

# import sys
# input = sys.stdin.readline
# t = int(input())
# for i in range(t):
#     result = 0
#     n, m = map(int, input().split())
#     l = list(map(int, input().split()))
#     imp = [0 for i in range(n)]
#     imp[m] = 1
#     while result < n:    
#         if l[0] == max(l):
#             result += 1
#             l.pop(0)
#             if imp[0] == 1:
#                 print(result)
#                 break
#             else:
#                 imp.pop(0)    
#         else:
#             l.append(l[0])
#             l.pop(0)
#             imp.append(imp[0])
#             imp.pop(0)