from collections import deque

def water_jug(cap1, cap2, target_state):
    visited = set()
    queue = deque()

    # queue stores (jug1, jug2, path)
    queue.append((0, 0, []))
    visited.add((0, 0))

    while queue:
        j1, j2, path = queue.popleft()

        current_path = path + [(j1, j2)]

        # check if target state is reached
        if (j1, j2) == target_state:
            return current_path

        # generate all possible next moves
        next_moves = [
            (cap1, j2),  # Fill jug 1
            (j1, cap2),  # Fill jug 2
            (0, j2),     # Empty jug 1
            (j1, 0),     # Empty jug 2

            # Pour jug 1 -> jug 2
            (
                j1 - min(j1, cap2 - j2),
                j2 + min(j1, cap2 - j2)
            ),

            # Pour jug 2 -> jug 1
            (
                j1 + min(j2, cap1 - j1),
                j2 - min(j2, cap1 - j1)
            )
        ]

        for move in next_moves:
            if move not in visited:
                visited.add(move)
                queue.append((move[0], move[1], current_path))

    return None


# Jug 1 = 4L
# Jug 2 = 3L
# Goal = (4,2)

target_goal = (4, 2)

solution = water_jug(4, 3, target_goal)

if solution:
    print(f"Steps to reach target state {target_goal}:")

    for step in solution:
        print(step)
else:
    print("No solution exists")