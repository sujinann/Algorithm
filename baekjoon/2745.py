N, B = input().split()
number = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
R = 0
for i in range(len(N)):
    R += (number.index(N[i])+1)*(int(B)**(len(N)-1-i))
print(R)