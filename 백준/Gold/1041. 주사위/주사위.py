n = int(input())
dice = list(map(int, input().split()))

two = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (2, 5), (3, 5), (4, 5), (1, 2), (2, 4), (3, 4), (1, 3)]
three = [(0,1,2), (0,1,3), (0,2,4), (0,3,4), (5,1,2), (5,1,3), (5,2,4), (5,3,4)]

answer = 0
if n == 1:
    answer = sum(dice) - max(dice)
else:
    INF = float('INF')
    min_three = INF
    min_two = INF
    for i in range(8):
        if dice[three[i][0]] + dice[three[i][1]] + dice[three[i][2]] < min_three:
            min_three = dice[three[i][0]] + dice[three[i][1]] + dice[three[i][2]]

    for i in range(12):
        if dice[two[i][0]] + dice[two[i][1]] < min_two:
            min_two = dice[two[i][0]] + dice[two[i][1]]

    answer = 4 * min_three + (8*(n-1)-4) * min_two + (4*((n-2)**2+n-2)+(n-2)**2) * min(dice)

print(answer)