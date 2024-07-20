n, k = map(int, input().split())

st = str(n)
l = len(st)

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = ''
before = set()

def check():
    global st, answer
    l = len(st)
    visited = [False] * l

    for i in range(l):
        if int(st[i]) not in before:
            before.add(int(st[i]))
            if len(before) > k:
                before.remove(int(st[i]))
                temp_list = list(before)
                temp_list.sort()
                for t in temp_list:
                    if t > int(st[i]):
                        answer = st[:i] + str(t) + str(min(before))  * (l-len(st[:i])-1)
                        print(int(answer))
                        quit()

                st = str(int(st[:i+1]) + 1) + '0' * len(st[i+1:])
                before.clear()
                check()
        else:
            visited[i] = True

    if len(before) < k:
        cnt = 0
        for i in range(l):
            if visited[l-1-i] == True:
                cnt += 1
                if k - len(before) == cnt:
                    st = str(int(st[:l-i]) + 1) + '0' * len(st[l-i:])
                    before.clear()
                    check()

    elif len(before) == k:
        print(int(st))
        quit()


if l < k:
    number.remove(1)
    answer = '1'
    for i in range(k-1):
        answer += str(number[i])
    print(int(answer))

else:
    check()