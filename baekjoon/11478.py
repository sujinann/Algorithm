s = str(input().strip())
ref = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        ref.add(s[i:j+1])
print(len(ref))