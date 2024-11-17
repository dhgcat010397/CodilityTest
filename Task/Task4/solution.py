# Problem: https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    time = -1

    # Find the all index of X in array A
    list_idx = []
    for idx, pos in enumerate(A):
        if pos == X:
            list_idx.append(idx)

    # A[:idx] is list of positions from 0 second to idx second
    # list(range(1,X)) is list of positions from 1 to X
    for idx in list_idx:
        if set(list(range(1, X))).issubset(set(A[:idx])):
            time = idx

    return time
