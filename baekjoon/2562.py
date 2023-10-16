l = []
cnt = 0
for i in range(1, 10) :
    l.append(int(input()))
print(max(l))

for i in l :
    if i < max(l) :
        cnt += 1
    elif i == max(l) :
        break
print(cnt+1)