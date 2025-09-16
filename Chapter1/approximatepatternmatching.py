import sys 
'''
Input: Strings Pattern and Text along with an integer d.
Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
'''
def approximate_pattern_matching(pattern: str, text: str, d: int) -> list[int]:
    """Find all starting positions where Pattern appears as a substring of Text with at most d mismatches."""
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i+len(pattern)]
        if hamming(substring,pattern) <= d:
            positions.append(i)
    return positions

def hamming(s: str, t: str) -> int:
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count+=1
    return count