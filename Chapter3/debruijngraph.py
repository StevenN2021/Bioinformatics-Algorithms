h
'''
Input: A collection of k-mers Patterns.
Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
'''

def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a collection of k-mers."""
    debruijn: Dict[str, List[str]] = {}
    k = len(k_mers[0])

    for pattern in k_mers: 
        suffix = pattern[-(k-1):]
        prefix = pattern[:k-1]
        if prefix not in debruijn:
            debruijn[prefix] = [suffix]
        else:
            debruijn[prefix].append(suffix)
    return debruijn