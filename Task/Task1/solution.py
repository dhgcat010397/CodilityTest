from typing import Counter

def check_valid(S):
    import re
    return re.match(r'^[a-z]+$', S) is not None

def solution(S):
    if not check_valid(S):
        return -1 
    
    all_substrings = []

    # Find all substrings of the given string S
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if i != j:
                all_substrings.append(S[i:j+1])

    # Get frequency of substrings
    freq = Counter(all_substrings)

    # Store all substrings which has frequency equal to 1 into a list
    min_freq = []
    for i in freq:
        if freq[i] == 1:
            min_freq.append(i)

    # Get a hashmap with key is substring and value is the length of the substring
    hashmap = dict()
    for i in range(len(min_freq)):
        hashmap[min_freq[i]] = len(min_freq[i])

    return min(hashmap.values())

