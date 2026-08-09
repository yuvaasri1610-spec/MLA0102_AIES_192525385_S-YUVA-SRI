def alphabeta(depth, node, alpha, beta, is_max):
    if depth == 0:
        return node

    if is_max:
        value = float('-inf')

        for child in node:
            value = max(value, alphabeta(depth-1, child,
                                         alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(value, alphabeta(depth-1, child,
                                         alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


tree = [[3, 5], [2, 9]]

result = alphabeta(2, tree, float('-inf'),
                   float('inf'), True)

print("Best value:", result)
