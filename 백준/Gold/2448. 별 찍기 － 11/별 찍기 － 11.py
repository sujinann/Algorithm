n = int(input())

t = n // 3
k = 0
while t > 1:
    t //= 2
    k += 1

tri = ['  *  ', ' * * ', '*****']

for i in range(k):
    temp = []
    for tr in tri:
        temp.append(' '*3*(2**i) + tr + ' '*3*(2**i))

    for tr in tri:
        temp.append(tr + ' ' + tr)

    tri = temp

for i in tri:
    print(i)