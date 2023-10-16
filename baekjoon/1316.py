N = int(input())

for i in range(N):
    S = input()
    for i in range(len(S)-1) :
        if S[i] == S[i + 1]:
           continue
        else:
            if S[i] in S[i + 1 : ]:
                N -= 1
                break

print(N)
