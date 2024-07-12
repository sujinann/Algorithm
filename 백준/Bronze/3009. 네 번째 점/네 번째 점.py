v = []
for i in range(3):
    v.append(list(map(int, input().split())))
    
answer = []
if v[0][0] == v[1][0]:
    answer.append(v[2][0])
else:
    if v[0][0] == v[2][0]:
        answer.append(v[1][0])
    else:
        answer.append(v[0][0])
        
if v[0][1] == v[1][1]:
    answer.append(v[2][1])
else:
    if v[0][1] == v[2][1]:
        answer.append(v[1][1])
    else:
        answer.append(v[0][1])
        
print(*answer)