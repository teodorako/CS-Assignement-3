#PERM - Enumerating Gene Orders by Teodora Kovacevic

from itertools import permutations

n = 5
counter = 0 
perm = permutations([item for item in range(1,n+1)]) 
   
for item in list(perm): 
    item = str(item).replace(",", "")
    item = item.replace("(","")
    item = item.replace(")","")
    print(item)
    counter+=1
print(counter)