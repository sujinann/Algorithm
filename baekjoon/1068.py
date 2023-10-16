# N = int(input())
# lists = list(map(int, input().split()))
# target = int(input())

# tree = [[] for i in range(N)]
# visited = [0] * N
# for i in range(N):
#     if lists[i] != -1:
#         tree[lists[i]].append(i)

# for i in range(N):
#     if target in tree[i]:
#         tree[i].remove(target)

# tree[target] = []
   


# def dfs(x):
#     for i in tree[x]:

#         if len(tree[i]) == 0:
#             visited[i] = 1
#         else:
#             dfs(i)


# dfs(0)

# answer = sum(visited)


# print(answer)



import sys
input = sys.stdin.readline

def dfs(num):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0

dfs(k)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)


















# cnt = 0
# for i in range(N):
#     cnt += 1
#     if lists[i] != -1 and not visited[lists[i]]:
#         visited[lists[i]] = True
#         cnt -= 1
#
# target = int(input())
