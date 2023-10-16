N, B = map(int, input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
A = ''
while N != 0:
    A += str(num[N % B])
    N = N // B
print(A[::-1])