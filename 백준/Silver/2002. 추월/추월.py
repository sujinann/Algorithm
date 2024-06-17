n = int(input())

start = []
end = []
for t in range(n):
    start.append(input())

for t in range(n):
    end.append(input())

answer = 0
sidx = 0
eidx = 0

passed = []

while sidx < n and eidx < n:
    if start[sidx] != end[eidx]:
        if len(passed) > 0:
            if start[sidx] in passed:
                passed.remove(start[sidx])
                sidx += 1
                continue
        answer += 1
        passed.append(end[eidx])
        eidx += 1

    else:
        sidx += 1
        eidx += 1

print(answer)