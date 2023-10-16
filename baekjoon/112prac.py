colwidth = 61
rule90 = {'000':'0', '001':'1', '010':'0', '011':'1', '100':'1', '101':'0', '110':'1', '111':'0'}

half = colwidth // 2
line = '0' * half + '1' + '0' * half
print(line)

while line[1] == '0':
    preline = line
    line = '0'
    for i in range(30):
        temp = ''
        for j in range(3):
            temp += preline[i+j]
        line += rule90[temp]
    rest = line[0:30]
    line += rest[::-1]
    print(line)