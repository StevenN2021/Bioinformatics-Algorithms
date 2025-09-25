from immediateneighbors.py import neighbors 
from immediateneighbors.py import hamming
'''
Input: Integers k and d, followed by a space-separated collection of strings Dna.
Output: All (k, d)-motifs in Dna.
'''
def motif_enumeration(dna: list[str], k: int, d: int) -> list[str]:
    
    res = set()
    first_seq = dna[0]
    n = len(first_seq)
    for i in range(n-k+1):
        pattern = first_seq[i:i+k]
        neighborhood = neighbors(pattern,d)
        for neighbor in neighborhood:
            if all(any(hamming(neighbor, seq[j:j+k]) <= d for j in range(len(seq)-k+1)) for seq in dna):
                res.add(neighbor)
                
    return list(res)
