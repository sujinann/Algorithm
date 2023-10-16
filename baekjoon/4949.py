import sys
input = sys.stdin.readline
while True:
    s = input().rstrip()
    l = []
    if s == '.':
            break
    for i in s:
        if i == '(' or i == '[':
            l.append(i)
        elif i == ')':
            if '(' in l:
                if l[len(l)-1] == '(':
                    l.pop()
                else:
                    break
            else:
                l.append(i)
                break
        elif i == ']':
            if '[' in l:
                if l[len(l)-1] == '[':
                    l.pop()
                else:
                    break
            else:
                l.append(i)
                break
    if len(l) == 0:
        print('yes')
    else:
        print('no')