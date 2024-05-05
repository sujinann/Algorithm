n = int(input())

def find(n):
    queue = [i for i in range(1, 10)]
    count = 0

    while queue:
        current = queue.pop(0)
        count += 1

        if count == n:
            return current

        last_digit = current % 10
        for next_digit in range(last_digit):
            queue.append(current * 10 + next_digit)

if n == 0:
    print(0)
else:
    if find(n):
        print(find(n))
    else:
        print(-1)