t = int(input())
for tc in range(t):
    ax, ay, ar, bx, by, br = map(int, input().split())
    answer = 0
    if ax == bx and ay == by:
        if ar == br:
            answer = -1
    else:
        d = ((ax-bx)**2 + (ay-by)**2)**(1/2)
        if d == (ar+br):
            answer = 1
        elif d < (ar+br) and (ar < br + d) and (br < ar + d):
            answer = 2
        elif d < (ar+br) and ((ar == br + d) or (br == ar + d)):
            answer = 1

    print(answer)