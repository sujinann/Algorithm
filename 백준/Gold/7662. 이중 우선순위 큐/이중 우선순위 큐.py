import heapq


t = int(input())
for tc in range(t):
    k = int(input())

    mini = []
    maxi = []
    visited = [False] * 1000000

    for i in range(k):
        command, n = input().split()
        n = int(n)

        if command == 'I':
            heapq.heappush(mini, [n, i])
            heapq.heappush(maxi, [-n, i])
            visited[i] = True
        else:
            if n == -1:
                while mini and not visited[mini[0][1]]:
                    heapq.heappop(mini)
                if mini:
                    temp = heapq.heappop(mini)
                    visited[temp[1]] = False
            else:
                while maxi and not visited[maxi[0][1]]:
                    heapq.heappop(maxi)
                if maxi:
                    temp = heapq.heappop(maxi)
                    visited[temp[1]] = False

    while mini and not visited[mini[0][1]]:
        heapq.heappop(mini)
    while maxi and not visited[maxi[0][1]]:
        heapq.heappop(maxi)

    if mini:
        ans = -heapq.heappop(maxi)[0]
        wer = heapq.heappop(mini)[0]
        print(ans, wer)
    else:
        print("EMPTY")