l, r = input().split()

answer = 0

if len(l) == len(r):
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                answer += 1
        else:
            break

print(answer)