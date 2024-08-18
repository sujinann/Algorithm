n = int(input())

tree = {}
s = set()
nodes = []
for i in range(n):
    a, b, c = input().split()

    tree[a] = [b, c]
    nodes.append(a)
    s.add(b)
    s.add(c)

root = ''
for node in nodes:
    if node not in s:
        root = node
        break

preanswer = ''
def preorder(x):
    global preanswer
    if x == '.':
        return
    
    preanswer += x
    
    for i in tree[x]:
        preorder(i)

inanswer = ''
def inorder(x):
    global inanswer
    if x == '.':
        return
    
    for i in range(2):
        if i == 1:
            inanswer += x
        inorder(tree[x][i])
    
postanswer = ''
def postorder(x):
    global postanswer
    if x == '.':
        return

    for i in tree[x]:
        postorder(i)

    postanswer += x


preorder(root)
inorder(root)
postorder(root)

print(preanswer)
print(inanswer)
print(postanswer)