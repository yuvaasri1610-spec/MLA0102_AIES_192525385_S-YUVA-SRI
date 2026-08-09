def minimax(depth, node, is_max):
    if depth == 0:
        return node

    if is_max:
        return max(minimax(depth-1, node[0], False),
                   minimax(depth-1, node[1], False))
    else:
        return min(minimax(depth-1, node[0], True),
                   minimax(depth-1, node[1], True))


tree = [[3, 5], [2, 9]]

result = minimax(2, tree, True)

print("Best value:", result)
