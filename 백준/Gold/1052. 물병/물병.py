n, k = map(int, input().split())

def check(x):
    a = x
    count = 0
    while a > 0:
        count += a % 2
        a //= 2

    return count

answer = 0
if n > k:
    i = n
    while True:
        if check(i) <= k:
            answer = i - n
            break
        i += 1

print(answer)