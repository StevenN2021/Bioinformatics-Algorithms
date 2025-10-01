def greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Implements the GreedyMotifSearch algorithm."""
    best_motifs = [seq[:k] for seq in dna]
    n = len(dna[0])

    for i in range(n - k + 1):
        motifs = [dna[0][i:i + k]]
        for j in range(1, t):
            profile = generate_profile(generate_counts(motifs))
            next_motif = profile_most_probable_kmer(dna[j], k, profile)
            motifs.append(next_motif)
        consensus = generate_consensus_string(generate_profile(generate_counts(motifs)))
        if generate_score(motifs, consensus) < generate_score(best_motifs, generate_consensus_string(generate_profile(generate_counts(best_motifs)))):
            best_motifs = motifs

    return best_motifs

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
    consensus = ""
    for col in profile:
        max_nuc = max(col, key=col.get)
        consensus += max_nuc
    return consensus
def generate_counts(Motifs: list[str]) -> list[dict[str, int]]:
    #each dict in the list of dicts corresponds to one col of motifs matrix 
    rows = len(Motifs)
    cols = len(Motifs[0])
    res = [{}]
    for i in range(cols):
        col_count = {"A": 0, "C": 0, "G": 0, "T": 0}
        for j in range(rows): 
            col_count[Motifs[j][i]] += 1
        res.append(col_count)
    return res
def generate_profile(counts: list[dict[str, int]]) -> list[dict[str, float]]:
    profile = []
    for col in counts:
        col_total = sum(col.values())
        col_profile = {nuc: count / col_total for nuc, count in col.items()}
        profile.append(col_profile)
    return profile
def generate_score(motifs: list[str], consensus: str) -> int:
    score = 0
    for motif in motifs:
        for i in range(len(motif)):
            if motif[i] != consensus[i]:
                score += 1
    return score