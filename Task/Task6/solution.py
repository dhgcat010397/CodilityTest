'''
    Problem: DominoSequence
    Source: Codility_algo_mid.pdf
'''

def solution(A):
    N = len(A) // 2  # length of domino tiles create from A
    domino_tiles = []
    for k in range(N):
        domino_tiles.append((A[2*k], A[2*k+1]))

    count_list = []   # the minimum number of domino tiles that must be removed from the sequence so that the remaining tiles form a correct domino sequence
    # prev_dot = domino_tiles[0][-1]
    for i in range(0, len(domino_tiles)-1):
        prev_dot = domino_tiles[i][-1]
        count = i
        for j in range(i+1, len(domino_tiles)):
            if prev_dot != domino_tiles[j][0]:
                count += 1
            else:
                prev_dot = domino_tiles[j][-1]
        count_list.append(count)

    return min(count_list) if len(count_list) > 0 else 0
