#REVP - Locating Restriction Sites by Teodora Kovacevic

from Bio.Seq import Seq
from Bio import SeqIO

fasta_seq = SeqIO.read("rosalind_revp.txt", "fasta")
sequence = str(fasta_seq.seq)

def palindrome(sequence):
    results = []
    for i in range(len(sequence)):
        for j in range(4, 13):
            if i + j <= len(sequence):
                substring = sequence[i:i+j]
                reverse_complement = Seq(substring).reverse_complement()
                if substring == reverse_complement:
                    results.append((i + 1, j))
    return results

result = palindrome(sequence)

for position, length in result:
    print(str(position) + ' ' + str(length))

