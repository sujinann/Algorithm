n = int(input())
words = []
for i in range(n):
    words.append(input())

visited = [1] * n
for i in range(n):
    if visited[i] == 1:
        for j in range(i+1, n):
            if visited[j] == 1:
                if len(words[i]) <= len(words[j]):
                    if words[i] == words[j][:len(words[i])]:
                        visited[i] = 0
                        break
                else:
                    if words[j] == words[i][:len(words[j])]:
                        visited[j] = 0

print(sum(visited))