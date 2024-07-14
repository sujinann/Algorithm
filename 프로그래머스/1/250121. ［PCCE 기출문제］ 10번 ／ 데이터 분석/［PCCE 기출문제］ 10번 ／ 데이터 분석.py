def solution(data, ext, val_ext, sort_by):
    answer = []
    
    e = -1
    if ext[0] == 'c':
        e = 0
    elif ext[0] == 'd':
        e = 1
    elif ext[0] == 'm':
        e = 2
    else:
        e = 3
        
    s = -1
    if sort_by[0] == 'c':
        s = 0
    elif sort_by[0] == 'd':
        s = 1
    elif sort_by[0] == 'm':
        s = 2
    else:
        s = 3
        
    for d in data:
        if d[e] < val_ext:
            answer.append(d)
            
    answer.sort(key = lambda x : x[s])
    
    
    return answer