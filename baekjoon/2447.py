# import sys
# input = sys.stdin.readline
# def append_star(LEN):
#     if LEN == 1:
#         return ['*']

#     Stars = append_star(LEN//3) 
#     L = []      
#     for S in Stars:
#         L.append(S*3)
#     for S in Stars:
#         L.append(S+' '*(LEN//3)+S)
#     for S in Stars:
#         L.append(S*3)
#     return L

# n = int(input())
# print('\n'.join(append_star(n)))
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
while n!=1:
    n = n//3
    cnt += 1

temp = '*'
for j in range(cnt):
    l = []
    for i in temp:
        l.append(i*3)
    for i in temp:
        l.append(i+' '*len(temp) +i)
    for i in temp:
        l.append(i*3)
    temp = l
print('\n'.join(temp))