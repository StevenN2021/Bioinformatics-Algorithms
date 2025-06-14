import sys
'''
Code Challenge: Solve the Frequent Words Problem.

Input: A string Text and an integer k.
Output: All most frequent k-mers in Text.
'''
def frequent_words(text: str, k: int) -> list[str]:
    kmers = {}
    result = [] 
    for i in range(len(text) - k+1):
        if text[i:i+k] not in kmers.keys():
            kmers[text[i:i+k]] = 1
        else:
            kmers[text[i:i+k]] += 1
    
    #find max and include ties
    max_val = max(kmers.values())
    for key,value in kmers.items():
        if value == max_val:
            result.append(key) 
    
    return result
