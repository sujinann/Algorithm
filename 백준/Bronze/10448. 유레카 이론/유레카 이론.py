t = int(input())
tri = []
eureka = [0] * 1001

for i in range(1, 100):
    if i*(i+1)//2 <= 1000:
        tri.append(i*(i+1)//2)
    else:
        break

for i in tri:
    for j in tri:
        for k in tri:
            if i + j + k <= 1000:
                eureka[i+j+k] = 1
            else:
                break
        if i + j > 1000:
            break

for i in range(t):
    print(eureka[int(input())])