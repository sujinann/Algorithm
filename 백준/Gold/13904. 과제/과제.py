n = int(input())

l = [[] for i in range(1001)]
days = set()

for i in range(n):
    d, w = map(int, input().split())
    l[d].append(w)
    days.add(d)

answer = []

days = list(days)
days.sort()

for day in days:
    if len(answer) + len(l[day]) <= day:
        answer += l[day]

    else:
        m = len(answer) + len(l[day]) - day
        answer += l[day]
        answer.sort()
        answer = answer[m:]

print(sum(answer))