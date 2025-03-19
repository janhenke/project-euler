"""A module defining number permutation functions."""


def nth_permute_lexicographically(sequence, n):
    """Return the nth lexicographically permutation of the given sequence.

    Note that the algorithm works in place on the sequence.
    :param sequence: The sequence (list) to permute
    :param n: The amount of permutations
    """
    for i in range(n + 1):
        permute_lexicographically(sequence)


def permute_lexicographically(sequence):
    """Return the next lexicographically permutation of the given sequence.

    Note that the algorithm works in place on the sequence.
    :param sequence: The sequence (list) to permute
    """
    n = len(sequence)
    k = 0
    for i in range(n - 1):
        if sequence[i] < sequence[i + 1]:
            k = i

    l = k + 1
    for i in range(k + 1, n):
        if sequence[k] < sequence[i]:
            l = i

    sequence[k], sequence[l] = sequence[l], sequence[k]
    temp = sequence[k + 1:]
    temp.reverse()
    sequence[k + 1:] = temp
