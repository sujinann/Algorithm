while True:
    m = int(input())
    if m == 0:
        break
    s = input()
    answer = 0

    d = dict()
    j = 0
    for i in range(len(s)):
        if len(d) < m:
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        else:
            if s[i] in d:
                d[s[i]] += 1
            else:
                while len(d) >= m and i > j:
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        del d[s[j]]
                    j += 1
                d[s[i]] = 1

        if sum(d.values()) > answer:
            answer = sum(d.values())

    print(answer)