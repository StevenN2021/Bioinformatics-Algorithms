import random 

def randomized_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Implements the RandomizedMotifSearch algorithm with pseudocounts."""
    best_motifs = random_kmers()
    while True:
        prof = generate_profile(generate_counts(best_motifs))
#helper to randomly choose set of kmers in dna 
def random_kmers(dna: list[str], k: int) -> list[str]:
    res = []
    for seq in dna: 
        start = random.randint(0, len(seq) - k)
        res.append(seq[start:start + k])
    return res

#helper for generate_score 
def generate_consensus_string(profile: list[dict[str, float]]) -> str:
    consensus = ""
    for col in profile:
        max_nuc = max(col, key=col.get)
        consensus += max_nuc
    return consensus

#helper for generate_profile
def generate_counts(Motifs: list[str]) -> list[dict[str, int]]:
    #each dict in the list of dicts corresponds to one col of motifs matrix 
    rows = len(Motifs)
    cols = len(Motifs[0])
    res = [{}]
    for i in range(cols):
        col_count = {"A": 1, "C": 1, "G": 1, "T": 1}
        for j in range(rows): 
            col_count[Motifs[j][i]] += 1
        res.append(col_count)
    return res

#helper for greedy_motif_search
def generate_profile(counts: list[dict[str, int]]) -> list[dict[str, float]]:
    profile = []
    for col in counts:
        col_total = sum(col.get(nuc, 0) for nuc in "ACGT")
        if col_total == 0:
            col_profile = {nuc: 0.25 for nuc in "ACGT"}
        else:
            col_profile = {nuc: col.get(nuc, 0) / col_total for nuc in "ACGT"}
            profile.append(col_profile)
    return profile

#helper for greedy_motif_search
def generate_score(motifs: list[str], consensus: str) -> int:
    score = 0
    for motif in motifs:
        for i in range(len(motif)):
            if motif[i] != consensus[i]:
                score += 1
    return score