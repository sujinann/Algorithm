t = int(input())

for tc in range(t):
    s = input()
    answer = ""
    l = list(map(str, s))
    point = -1
    
    for i in range(len(s)-1):
        if s[len(s)-i-1] > s[len(s)-i-2]:
            point = len(s)-i-2
            break

    if point != -1:
        for i in range(len(s)):
            if s[point] < s[len(s)-i-1]:
                temp = s[point]
                l[point] = s[len(s)-i-1]
                l[len(s)-i-1] = temp

                left = l[:point+1]
                right = l[point+1:]
                right.sort()

                l = left + right
                break

    for i in l:
        answer += i

    print(answer)