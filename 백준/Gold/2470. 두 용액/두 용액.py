n = int(input())

l = list(map(int, input().split()))
l.sort()

left = 0
right = len(l) - 1

check = l[left] + l[right]
answer = [l[left], l[right]]

while left < right:
    temp = l[left] + l[right]
    if abs(temp) < abs(check):
        answer = [l[left], l[right]]
        check = temp

    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1
    else:
        answer = [l[left], l[right]]
        break

print(answer[0], answer[1])