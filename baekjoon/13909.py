# import sys
# input = sys.stdin.readline
# n = int(input())
# l = [0]*(n+1)
# for j in range(n):
#     for i in range(j+1, n+1, j+1):
#         if l[i] == 0:
#             l[i] = 1
#         else :
#             l[i] = 0
# print(l.count(1))         메모리초과


# 제곱수 구하기인데...너무 비효율적으로 품
n = int(input())
a = 1
s = 0
cnt = 0
for i in range(1, 2100000001):
    s += a
    if s == n:
        cnt += 1
        break
    elif s > n:
        break
    else:
        a += 2
        cnt += 1
print(cnt)