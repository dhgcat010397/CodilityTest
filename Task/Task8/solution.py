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

# from itertools import permutations

# def solution(AA, AB, BB):
#     str_AA = ["AA"] * AA
#     str_AB = ["AB"] * AB
#     str_BB = ["BB"] * BB
#     str_list = str_AA + str_AB + str_BB

#     sequence_list = []

#     sequence_len = len(str_list)
#     while sequence_len > 0:
#         permutations_ = permutations(str_list, sequence_len)
#         for perm in permutations_:
#             sequence = "".join(perm)
#             if "AAA" not in sequence and "BBB" not in sequence:
#                 sequence_list.append(sequence)
#         sequence_len -= 1

#     sequence_list = list(set(sequence_list))
    
#     print(f"All sequences: {sequence_list}")
#     longest_sequences = [s for s in sequence_list if len(s) == max(map(len, sequence_list))]
#     print(f"Length of longest sequence: {len(longest_sequences[0]) if len(longest_sequences) > 0 else 0}")   
#     return longest_sequences

def add_AA(str, AA):
    result = ""

    return result

def add_AB(str, AB):
    result = ""
    
    return result

def add_BB(str, BB):
    result = ""
    
    return result

def solution(AA, AB, BB):
    '''
    AA -> 	AABB
    BB -> 	BBAA
	        BBAB
    AB -> 	ABAA
	        ABAB
    '''
    
    sAA = [""] # string start with "AA"
    sAB = [""] # string start with "AB"
    sBB = [""] # string start with "BB"

    if AA > 0:
        sAA.append("AA")
    if AB > 0:
        sAB.append("AB")
    if BB > 0:
        sBB.append("BB")
    
    # with sAA
    if BB > 0:
        add_BB(sAA, AA-1, AB, BB)

    return 0
