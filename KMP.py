#KMP - Speeding Up Motif Finding by Teodora Kovacevic

import re

dataset = ">Rosalind_87CAGCATGGTATCACAGCAGAG"
sequence = " ".join(re.findall(r'[ATGC]+', dataset))

def failure(s):
    array_p = [0] * len(s)
    j = 0
    for k in range(2, len(s)+1):
        while j > 0 and s[j] != s[k-1]:
            j = array_p[j-1]
        if s[j] == s[k-1]:
            j += 1
        array_p[k-1] = j
    
    return array_p

result = failure(sequence)
print(" ".join(map(str, result)))
