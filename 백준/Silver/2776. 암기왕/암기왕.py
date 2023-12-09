def binary(x):
    start = 0
    end = n - 1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if note_one[mid] >= x:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    if x == note_one[result]:
        print(1)
    else:
        print(0)

t = int(input())
for tc in range(t):
    n = int(input())
    note_one = list(map(int, input().split()))
    note_one.sort()
    m = int(input())
    note_two = list(map(int, input().split()))

    for i in range(m):
        binary(note_two[i])
