from immediateneighbors.py import neighbors 
from immediateneighbors.py import hamming
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
            if neighbor not in freqs:
                freqs[neighbor] = 1
            else:
                freqs[neighbor] += 1 
    maxfreq = max(freqs.values()) 
    for pattern, freq in freqs.items():
        if freq == maxfreq:
            res.append(pattern)


  
