def dfs(x, visited, index):
   if len(visited) == 6:
       print(*visited)
       return

   if index == len(x):
       return
   
   if len(visited) == 0 and len(x) - index < 6:
       return
   
   for i in range(index, len(x)):
       visited.append(x[i])
       dfs(x, visited, i+1)
       visited.pop()


while True:
    l = list(map(int, input().split()))
    if l == [0]:
        break

    k = l[0]
    s = l[1:]

    dfs(s, [], 0)
    print()