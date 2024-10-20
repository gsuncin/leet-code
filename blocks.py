#input [2, 4, 3, 1, 6]

def check_list_ordered(blocks: list[int]):
    if blocks == sorted(blocks):
        return True

def order_blocks(blocks: list[int], moves=0):
    if len(blocks) == 1:
        return 0
    for i, el in enumerate(blocks):
        if i == len(blocks) - 1:
            break
        if el > blocks[i + 1]:
            blocks[i], blocks[i + 1] = blocks[i + 1], blocks[i]
            moves = order_blocks(blocks, moves=(moves+1))
    return moves

def get_min_moves(blocks: list[int]):
    moves = order_blocks(blocks)
    moves = moves -1
    if moves != 1:
        return moves
    return moves
ordered = get_min_moves([2, 4, 3, 1, 6])
ordered = get_min_moves([5, 4, 11, 9, 10, 12])
print(ordered)