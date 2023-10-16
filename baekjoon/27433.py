n = int(input())

def fac(x):
    if x > 0:
        return x*(fac(x-1))
    elif x == 0:
        return 1
print(fac(n))