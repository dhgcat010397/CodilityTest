'''
    There are two-letter strings, "AA", "AB" and "BB", which appear AA, AB and BB times respectively.
    The task is to join some of these strings to create the longest possible string which does not contain "AAA" and "BBB".
    
    For example, having AA = 5, AB = 0 and BB = 2, it is possible to join five strings by taking both of the "BB" strings and
    three of the "AA" strings. Then they can be joined into "AA-BB-AA-BB-AA" -> "AABBAABAA"
    
    Note that it is not possible to add another "AA" string as the result would then contain "AAA".

    Write a function
        def solution(AA, AB, BB)
    that, given three integers AA, AB and BB, returns the longest string that can be created by according to the rules described
    above. If there is more than one possible answer, the function may return any of them.
'''

from itertools import permutations

def solution(AA, AB, BB):
    str_AA = ["AA"] * AA
    str_AB = ["AB"] * AB
    str_BB = ["BB"] * BB
    str_list = str_AA + str_AB + str_BB

    sequence_list = []

    sequence_len = len(str_list)
    while sequence_len > 0:
        permutations_ = permutations(str_list, sequence_len)
        for perm in permutations_:
            sequence_list.append("".join(perm))
        sequence_len -= 1

    sequence_list = list(set(sequence_list))

    valid_sequence_list = []
    for sequence in sequence_list:
        if "AAA" not in sequence and "BBB" not in sequence:
            valid_sequence_list.append(sequence)
    
    print(f"All sequences: {valid_sequence_list}")
    longest_sequences = [s for s in valid_sequence_list if len(s) == max(map(len, valid_sequence_list))]   
    return longest_sequences
