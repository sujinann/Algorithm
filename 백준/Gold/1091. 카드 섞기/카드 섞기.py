n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

card = [0, 1, 2] * (n // 3)
origin = card

answer = 0
flag = False
while True:
    if card == p:
        flag = True
        break
    new_card = []
    for i in range(n):
        new_card.append(card[s[i]])

    card = new_card
    answer += 1

    if card == origin:
        break

if not flag:
    answer = -1

print(answer)