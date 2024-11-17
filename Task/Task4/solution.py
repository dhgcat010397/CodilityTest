# Problem: https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    for idx in range(len(A)):
        if set(list(range(1, X+1))).issubset(set(A[:idx+1])):
            return idx

    return -1
