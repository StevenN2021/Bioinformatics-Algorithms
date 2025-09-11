import sys 

'''
Input: Two strings, Pattern and Genome.
Output: A collection of integers specifying all starting positions where Pattern appears as a substring of Genome.
'''

def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Find all occurrences of a pattern in a genome."""

    res = []
    for i in range(len(genome) - len(pattern)+1):

        # create substring to compare 
        sub = genome[i:i+len(pattern)]
        if sub == pattern: 
            res.append(i)
    return res

    