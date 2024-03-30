n, k = map(int, input().split())
l = list(map(int, input().split()))

check = [[] for i in range(100001)]
start = 0
answer = 0
for i in range(n):
    check[l[i]].append(i)
    if len(check[l[i]]) > k:
        if check[l[i]][-k-1] + 1 > start:
            start = check[l[i]][-k-1] + 1 

    if i + 1 - start > answer:
        answer = i + 1 - start


print(answer)