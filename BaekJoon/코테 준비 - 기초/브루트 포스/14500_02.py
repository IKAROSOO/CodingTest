N, M = map(int, input().split())
Paper = []

for i in range(N):
    rows = list(map(int, input().split()))
    Paper.append(rows)


def get_max_sum(Paper, N, M):
    shapes = [
        [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)],

        [(0, 0), (0, 1), (1, 0), (1, 1)],

        [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 1), (1, 1), (2, 1), (2, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 2), (1, 2), (2, 2), (2, 1)],
        [(0, 1), (0, 2), (1, 0), (1, 1)], [(0, 0), (1, 0), (1, 1), (1, 2)],

        [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 1), (1, 1), (1, 0), (2, 0)],

        [(0, 0), (0, 1), (0, 2), (1, 1)], [(1, 0), (0, 1), (1, 1), (2, 1)],
        [(1, 0), (0, 1), (1, 1), (1, 2)], [(0, 1), (1, 0), (1, 1), (2, 1)]
    ]

    max_sum = 0

    for i in range(N):
        for j in range(M):
            for shape in shapes:
                try:
                    sum_value = sum(Paper[i + dx][j + dy] for dx, dy in shape)
                    max_sum = max(max_sum, sum_value)
                except IndexError:
                    continue

    return max_sum

print(get_max_sum(Paper, N, M))