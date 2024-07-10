s = input()

l = []
cnt = 0
b = 1

for i in s:
    if i == '(':
        l.append([cnt-1, b])
        cnt = 0
    elif i == ')':
        temp = l.pop()
        cnt = cnt * temp[1] + temp[0]
    else:
        cnt += 1
        b = int(i)

print(cnt)