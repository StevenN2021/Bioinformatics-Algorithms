def greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Implements the GreedyMotifSearch algorithm."""
    pass

def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    res = ""
    prob = -1.0

    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        curr_prob = 1.0
        for j, nuc in enumerate(pattern):
            curr_prob *= profile[j][nuc]
        if curr_prob > prob:
            prob = curr_prob
            res = pattern

    return res

def generate_consensus_string(profile: list[dict[str, float]]) -> str:
    pass
def generate_counts(Motifs: list[str]) -> list[dict[str, int]]:
    #each dict in the list of dicts corresponds to one col of motifs matrix 
def generate_profile():
    pass
def generate_score():
    pass
    