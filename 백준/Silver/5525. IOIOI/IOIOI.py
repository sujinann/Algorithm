n = int(input())
m = int(input())
s = input()

l = []
i = 0
cnt = 0
while i < m:
    if s[i] == 'I':
        cnt = 0
        for j in range(i+1, m-1, 2):
            if s[j] == 'O' and s[j+1] == 'I':
                cnt += 1
            else:
                break

        if cnt != 0:
            l.append(cnt)
            i += cnt*2

    i += 1

answer = 0
for i in range(len(l)):
    if l[i] >= n:
        answer += (l[i] - n + 1)

print(answer)