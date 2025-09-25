'''
Input: A string Pattern and an integer d.
Output: The collection of strings Neighbors(Pattern, d).
'''

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
    return sum(s[i] != t[i] for i in range(len(s)))
      
    
    
  
  
  
