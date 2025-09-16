import sys 

'''
Input: Strings Text and Pattern.
Output: Count(Text, Pattern).
'''
def pattern_count(text: str, pattern: str) -> int:
    count = 0
    n = len(text)
    k = len(pattern)
    for i in range(n-k+1):
        substr = text[i:i+len(pattern)]
        if (substr == pattern):
            count += 1
    return count
