N = int(input())
B = 0
while N >= 0:
    if N % 5 == 0:
        B = B + N//5
        print(B)
        break
    else:
        N -= 3
        B += 1
else:
    print(-1)