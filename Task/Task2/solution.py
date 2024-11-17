def solution(moves):
    count = 0
    move_left = False
    if len(moves) == 0:
        return -1
    for idx, move in enumerate(moves):
        if move not in ["<", ">", "^", "v"]:
            return -1       
        if idx == 0:
            move_left = True
        match move:
            case '<':
                if move_left:
                    count += 1
            case '>':
                if idx != len(moves) - 1:
                    move_left = False
                else:
                    count += 1
            case _:
                if not move_left:
                    move_left = True
                count += 1
    return count

