arr = []
arr2 = []

for i in range(10):
    arr.append(int(input()))

for i in arr:
   arr2.append(i % 42)

print(len(set(arr2)))