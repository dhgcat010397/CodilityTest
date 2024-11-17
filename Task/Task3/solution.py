def check_valid(S):
    return set(S).issubset({'-', 'h', 'H'})

def solution(S):
    if not check_valid(S):
        return -1
    if len(S) == 1:
        return -1

    count = 0
    pos = list(S.upper())
    for i in range(len(pos)):
        if pos[i] == 'H':
            if i == 0 and pos[i+1] == 'H':
                return -1
            elif i > 0:
                if i != len(pos) - 1:
                    if pos[i-1] == pos[i+1] == 'H':
                        return -1
                    elif pos[i-1] == pos[i+1] == '-':
                        pos[i+1] = 'T'
                        count += 1
                    elif pos[i-1] == 'H' and pos[i+1] == '-':
                        pos[i+1] = 'T'
                        count += 1
                else:
                    if pos[i-1] == '-':
                        count += 1
    
    return count
