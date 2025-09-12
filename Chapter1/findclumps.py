import sys

'''
Input: A string Genome, and integers k, L, and t.
Output: All distinct k-mers forming (L, t)-clumps in Genome.
'''

def find_clumps(genome: str, k: int, l: int, t: int) -> list[str]:
    """Find patterns forming clumps in a genome."""
    res = set()
    for i in range(len(genome)-l+1):
        window = genome[i:i+l]
        freqs = freq_table(window,k)
        for key in freqs.keys():
            if freqs[key] >= t:
                res.add(key)
    
    return res
   
def freq_table(window: str, k: int) -> dict[str,int]: 
    res = {}
    for i in range(len(window)-k+1): 
        pattern = window[i:i+k]
        if pattern not in res: 
            res[pattern] = 1
        else:
            res[pattern] += 1
    return res
    