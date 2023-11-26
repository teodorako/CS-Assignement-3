#EUBT - Enumerating Unrooted Binary Trees by Teoodra Kovacevic

with open('rosalind_eubt.txt') as f:
    dataset = f.read().split()

def eubt(taxa):
    first_taxa, second_taxa, additional_taxa = taxa.pop(), taxa.pop(), taxa.pop()
    sub = {first_taxa, second_taxa}
    trees = {f'({first_taxa},{second_taxa}),{additional_taxa}'}

    while taxa:
        current_taxa, new_trees = taxa.pop(), set()

        for tree in trees:
            for s in sub:
                new_trees.add(tree.replace(s, f'({s},{current_taxa})'))

            count = 0
            for i, char in enumerate(tree):
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count == 0:
                        new_trees.add(tree[:i+1] + f',{current_taxa}' + tree[i+1:])
                        break

        sub.add(current_taxa)
        trees = new_trees

    trees = {f'({k});' for k in trees}
    return trees

result = eubt(dataset)
print(*result, sep='\n')


