import itertools

'''
Input: An integer k, followed by a space-separated collection of strings Dna.
Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. 
(If there are multiple such strings Pattern, then you may return any one.)
'''
def median_string(Dna: list[str], k: int) -> str:
    dist = float('inf')
    res = ""
    patterns = allstrings(k)
    for i in range(len(patterns)):
        pattern = patterns[i]
        if dist > distance_between_pattern_and_strings(pattern,Dna):
            dist = distance_between_pattern_and_strings(pattern,Dna)
            res = pattern
    return res



def allstrings(k):
    bases = ["A","T","C","G"]
    return [''.join(x) for x in product(bases,repeat = k)]

def distance_between_pattern_and_strings(Pattern: str, Dna: list[str]) -> int: 
    k = len(pattern)
    dist = 0
    for text in Dna: 
        ham = float('inf')
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            if ham > hamming(pattern,kmer):
                ham = hamming(pattern,kmer)
        dist += ham
    return dist

def hamming(s,t):
    return sum(s[i] != t[i] for i in range(len(s)))