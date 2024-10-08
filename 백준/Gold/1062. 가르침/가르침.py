n, k = map(int, input().split())
set_list = []
standard = set(['a', 'n', 't', 'i', 'c'])
for i in range(n):
    s = set(input())
    
    if len(s) <= k:
        set_list.append(s)

alpha = [False] * 26
for s in standard:
    alpha[ord(s) - ord('a')] = True

answer = 0

def check():
    cnt = 0
    for ss in set_list:
        flag = False
        for s in ss:
            if not alpha[ord(s) - ord('a')]:
                flag = True
                break

        if not flag:
            cnt += 1

    return cnt
        

def dfs(x, dep):
    global answer
    
    if dep == k:
        answer = max(answer, check())
        return
    
    for i in range(x+1, 26):
        if not alpha[i]:
            alpha[i] = True
            dfs(i, dep+1)
            alpha[i] = False

dfs(0, 5)
print(answer)