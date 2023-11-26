#PMCH - Perfect Matchings and RNA Secondary Structures by Teodora Kovacevic

from collections import Counter
from math import factorial
from Bio import SeqIO

with open("rosalind_pmch.txt", 'r') as f:
    dataset = SeqIO.read(f, "fasta")

sequence = str(dataset.seq)
counts = Counter(sequence)
number = factorial(counts["A"]) * factorial(counts["C"])

print(number)
