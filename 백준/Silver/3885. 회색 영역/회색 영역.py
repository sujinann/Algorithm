while True:
    n, w = map(int, input().split())
    if n == 0 and w == 0:
        break

    count = [0] * 11
    maxi = 0
    for i in range(n):
        v = int(input())
        if v > maxi:
            maxi = v
        count[v // w] += 1

    h = max(count)
    d = maxi // w

    answer = 0.01
    for i in range(maxi // w + 1):
        answer += (count[i] / h) * ((d - i) / d)

    print(answer)