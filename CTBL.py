#CTBL - Creating a Character Table by Teodora Kovacevic

import re

with open('rosalind_ctbl.txt', 'r') as f:
    trees = f.read().strip()

def parsing(tree):
    return sorted(re.sub('[^0-9a-zA-Z_]+', ' ', tree).strip().split(' '))

def table(tree):
    char_table = []
    taxa = parsing(tree)
    taxa_dict = {i:taxa.index(i) for i in taxa}
    
    level = 0
    position = []
    subtrees = []
    
    for i in range(len(tree)):
        if tree[i] == '(':
            level += 1
            position.append(i)
        elif tree[i] == ')':
            subtree = tree[position[-1]+1:i]
            del position[-1]

            while len(subtrees) < level:
                subtrees.append([])
                
            subtrees[level-1].append(subtree)
            level -= 1
    
    for i in range(1, len(subtrees)):
        for j in subtrees[i]:
            char_table.append([0 for i in range(len(taxa_dict))])
            
            for k in parsing(j):
                char_table[-1][taxa_dict[k]] = 1

    return char_table

result = table(trees)
for m in result:
    print(''.join(map(str, m)))