a, b = map(int, input().split())

al = set(map(int, input().split()))
bl = set(map(int, input().split()))

answer = al - bl
answer = list(answer)
answer.sort()

print(len(answer))
if len(answer) != 0:
    print(*answer)