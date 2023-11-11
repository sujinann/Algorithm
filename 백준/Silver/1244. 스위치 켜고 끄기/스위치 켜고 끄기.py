n = int(input())
switch = list(map(int, input().split()))
c = int(input())

def turn(x):
    if switch[x] == 1:
        switch[x] -= 1
    else:
        switch[x] += 1

for i in range(c):
    s, g = map(int, input().split())
    if s == 1:
        if n//g >= 1:
            for j in range(1, n//g+1):
                turn(g*j-1)
        else:
            turn(g-1)
    else:
        cnt = 1
        while g-1-cnt>=0 and g-1+cnt<n and switch[g-1-cnt] == switch[g-1+cnt]: 
            turn(g-1-cnt)
            turn(g-1+cnt)
            cnt += 1
        turn(g-1)

for i in range(len(switch)):
    print(switch[i], end=' ')
    if i % 20 == 19:
        print()