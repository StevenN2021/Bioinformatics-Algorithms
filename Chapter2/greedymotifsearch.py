from profilemostprobablekmer import profile_most_probable_kmer

def greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Implements the GreedyMotifSearch algorithm."""
    best_motifs = [seq[:k] for seq in dna]
    n = len(dna)
    for i in range(len(dna[0]) - k + 1):
        kmer = dna[0][i:i+k]
        motifs = [kmer]
        for j in range(1,n):
            profile = generate_profile(generate_counts(motifs))
            next_kmer = profile_most_probable_kmer(dna[j], k, profile)
            motifs.append(next_kmer)
        if generate_score(motifs, generate_consensus_string(generate_profile(generate_counts(motifs)))) < generate_score(best_motifs, generate_consensus_string(generate_profile(generate_counts(best_motifs)))):
            best_motifs = motifs
    return best_motifs

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
        col_count = {"A": 0, "C": 0, "G": 0, "T": 0}
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