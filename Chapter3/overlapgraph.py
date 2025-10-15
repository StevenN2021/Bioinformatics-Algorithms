
'''
Input: A collection Patterns of k-mers.
Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the nodes and their edges in any order.)
'''

def overlap_graph(patterns: List[str]) -> Dict[str, List[str]]:
    """Forms the overlap graph of a collection of patterns."""
    suffixes = {}
    overlap = {}
    k = len(patterns[0])
    for pattern in patterns:
        suffix = pattern[-(k-1):]
        print(suffix) 
        suffixes[suffix] = pattern
    
    for kmer in patterns:
        prefix = kmer[:k-1]
        print(prefix) 
        to_append = []
        if prefix in suffixes:
            #kmer is the key 
            to_append.append(suffixes[prefix])
            overlap[kmer] = to_append
    return overlap 
