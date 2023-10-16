n, m = map(int, input().split())
did = {}
dname = {}
for i in range(1, n+1):
    a = input()
    did[a] = i
    dname[i] = a
for j in range(m):
    b = input()
    if b.isdigit():
        print(dname[int(b)])
    else :
        print(did[b])
# int 는 상관없지만 str는 strip붙여야함
# readline이 한줄 모두 입력받기 때문에 개행문자 같은 것도 같이가져오기때문


# import sys
# input = sys.stdin.readline
# + .strip()

# 위와 아래의 차이

# from sys import stdin
# def input():
#     return stdin.readline().rstrip()