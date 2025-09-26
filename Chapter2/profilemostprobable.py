
def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """
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
