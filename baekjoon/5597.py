arr = list(range(1, 31))

for i in range(28):
    arr.remove(int(input()))

print(min(arr))
print(max(arr))