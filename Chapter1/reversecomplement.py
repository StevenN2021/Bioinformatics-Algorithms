import sys
'''
Input: A DNA string Pattern.
Output: Patternrc , the reverse complement of Pattern.
'''

def reverse_complement(pattern: str) -> str:
    """Calculate the reverse complement of a DNA pattern."""
    comps = {
        "A" : "T",
        "G" : "C",
        "C" : "G",
        "T" : "A"
    }
    res = ""
    for char in pattern:
        res += comps[char]
    return res[::-1]

