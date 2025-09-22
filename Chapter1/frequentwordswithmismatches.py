from immediateneighbors.py import neighbors 
from 
'''
Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
Output: All most frequent k-mers with up to d mismatches in Text.
'''
def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    """Find the most frequent k-mers with up to d mismatches in a text."""
    res = [] 
    freqs = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern,d)
        for neighbor in neighborhood: 
            if freqs[neighbor] not in freqs:
                freqs[neighbor] = 1
            else:
                freqs[neighbor] += 1 
    max = max(freqs.values()) 
    for pattern, freq in freqs.items():
        if freq == max:
            res.append(pattern)
            
    return res 
def neighbors(s: str, d: int) -> list[str]:
    """Generate neighbors of a string within a given Hamming distance."""
    
    # base case 
    if d == 0:
        return {s}
    if len(s) == 1:
        return [s] if d == 0 else ["A","C","T","G"]
    
    res = set()
    suffix_neighbors = neighbors(s[1:],d) 
    
    for text in suffix_neighbors:
        if hamming(s[1:],text) < d: 
            for nuc in ["A","T","C","G"]:
                res.add(nuc + text) 
        else:
            res.add(s[0] + text)
              
    return res
    
 
    
def hamming(s: str, t: str) -> int:
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count+=1
    return count


  
