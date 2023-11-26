#PROB - Introduction to Random Strings by Teodora Kovacevic

import math

sequence = "AAAGGGATGAATGCGGATGGACAAATTGCGCTAGTGATACACCATGCGGGCGCTCATCCACGTGGCAATTTGCTCCAGAATGCTTGTAGAAAACGAGTTC"
dataset = "0.075 0.136 0.186 0.204 0.285 0.312 0.366 0.401 0.492 0.502 0.597 0.650 0.677 0.703 0.790 0.806 0.867 0.942"
dataset = dataset.strip()

def prob(sequence, gc_cont):
    gc_list = list(map(float, gc_cont.split()))
    result = []
    
    for gc in gc_list:
        probability = 1
        for base in sequence:
            if base in 'GC':
                probability *= gc / 2
            elif base in 'AT':
                probability *= (1 - gc) / 2
        
        result.append(round(math.log10(probability), 3))
    
    return result

result = prob(sequence, dataset)
print(" ".join(map(str, result)))
