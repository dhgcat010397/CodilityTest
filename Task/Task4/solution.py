# Problem: https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    list_pos = [-1]*X
    for idx, pos in enumerate(A):
        if list_pos[pos-1] == -1:
            list_pos[pos-1] = idx

    if -1 in list_pos:
        return -1
    else:
        return max(list_pos)
