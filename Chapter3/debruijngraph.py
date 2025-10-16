h
'''
Input: A collection of k-mers Patterns.
Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
'''

def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a collection of k-mers."""
    prefixes: Dict[str, List[str]] = {}
    k = len(k_mers[0])
    debruijn = {}
    for kmer in k_mers: 
        prefix = kmer[:k-1]
        if prefix in prefixes:
            prefixes[prefix].append(kmer)
        else:
            prefixes[prefix] = [kmer]

    for pattern in k_mers: 
        suffix = pattern[-(k-1):]
        prefix = pattern[:k-1]
        if suffix in prefixes:
            debruijn[pattern] = set([kmer for kmer in prefixes[suffix] if suffix == kmer[:k-1]])
    return debruijn