# import sys
# input = sys.stdin.readline
# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     for i in range(max(a, b), (a*b)+1):
#         if i % a == 0 and i % b == 0:
#             print(i)

# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     A, B = a, b
#     while b > 0:
#         a = a % b
#         a, b = b, a
#     print(A*B//a)

t = int(input())
for i in range(t):
    a, b = map(int, input().split()) #문제 입력값
    if a >= b:
        n = b
    else:
        n = a                        # min(a, b)
    l = [True] * (n + 1)
    m = int(n**0.5)

    for i in range(2, m + 1):
        if l[i] == True:
            for j in range(i + i, n + 1, i):
                l[j] = False        # 소수 이외 지우기

    l1 = set(i for i in range(2, n + 1) if l[i] == True)  # 소수 집합
    l2 = []
    for i in l1:
        while a%i == 0 and b%i == 0:
            a = a//i
            b = b//i
            l2.append(i)                # 소인수분해
    ans = 1
    for i in l2:
        ans *= i
    print(ans*a*b)          # 최소공배수