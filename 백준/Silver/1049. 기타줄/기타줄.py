n, m = map(int, input().split())
mins = float("inf")
mino = float("inf")
for i in range(m):
    six, one = map(int, input().split())
    if six < mins:
        mins = six
    if one < mino:
        mino = one

answer = 0
if 6 * mino <= mins:
    answer = mino * n
else:
    answer = n // 6 * mins
    if n % 6 * mino > mins:
        answer += mins
    else:
        answer += n % 6 * mino

print(answer)