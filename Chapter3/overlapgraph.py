
'''
Input: A collection Patterns of k-mers.
Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the nodes and their edges in any order.)
'''

def overlap_graph(patterns: List[str]) -> Dict[str, List[str]]:
    """Forms the overlap graph of a collection of patterns."""
    prefixes: Dict[str, List[str]] = {}
    overlap = {}
    k = len(patterns[0])
    for pattern in patterns:
        prefix = pattern[:k-1]
        if prefix in prefixes:
            prefixes[prefix].append(pattern)
        else:
            prefixes[prefix] = [pattern]
    
    for kmer in patterns:
        suffix = kmer[-(k-1):]
        to_append = []
        if suffix in prefixes:
            #kmer is the key 
            overlap[kmer] = set([pattern for pattern in prefixes[suffix] if suffix == pattern[:k-1]])
    return overlap 

