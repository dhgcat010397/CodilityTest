'''
    Problem: LongestTileSequence
    Source: Codility_algo_mid.pdf
'''

def solution(A):
    sequence_list = []
    for i in range(len(A)):
        tiles = [tile for idx, tile in enumerate(A) if idx != i]
        prev_tile = A[i]
        sequence = [prev_tile]
        for tile in tiles:
            if tile[0] == prev_tile[-1]:
                sequence.append(tile)
                prev_tile = tile
        sequence_list.append(sequence)
    # print(f"Longest sequence: {max(sequence_list, key=len)}")    
    return len(max(sequence_list, key=len))
