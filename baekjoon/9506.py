while True:
    n = int(input())
    if n == -1:
        break
    cnt = 0
    l = []
    sum = 0
    for i in range(1, n):
        if n % i == 0 :
            cnt += 1
            l.append(i)
            sum += i
    if sum == n:
        print(f'{n} = 1', end='')
        for i in range(1, cnt):
            print(f' + {l[i]}', end='')
        print()
    else :
        print(f'{n} is NOT perfect.')