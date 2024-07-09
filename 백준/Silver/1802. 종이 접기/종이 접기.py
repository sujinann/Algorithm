t = int(input())
for tc in range(t):
    s = input()

    answer = 'YES'

    for i in range(0, len(s), 2):
        if i < len(s)-2:
            if s[i] == s[i+2]:
                answer = 'NO'
                break

    for i in range(1, len(s)//2, 2):
        if s[i] == s[len(s)-i-1]:
            answer = 'NO'
            break

    print(answer)