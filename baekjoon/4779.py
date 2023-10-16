import sys
input = sys.stdin.readline
def can(n, s, f):
    if n == 0:
        return
    cut = (f-s+1)//3
    can(n-1, s, s+cut-1)
    for i in range(s+cut, s+cut*2):
        ans[i] = ' '
    can(n-1, s+cut*2, s+cut*3-1)

while True:
    try:
        n = int(input())
        ans = ['-']*(3**n)
        can(n, 0, 3**n-1)
        print(''.join(ans))
    except:
        break

# import sys
# input = sys.stdin.readline
# while True:
#     try:
#         n = int(input())
#         tmp = '-'
#         for i in range(n):
#             tmp = tmp+ ' '*len(tmp)+ tmp
#         print(tmp)
#     except:
#         break