def solution(k, d):
    answer = 0
    
    s = d // k
    
    start = s
    for i in range(s+1):
        for j in range(start, -1, -1):
            if (k*i)**2 + (k*j)**2 <= d**2:
                answer += j+1
                start = j
                break
    
    return answer