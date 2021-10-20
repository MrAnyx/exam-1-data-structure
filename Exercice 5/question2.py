# Author : Robin B

import math
import numpy as np

compact_matrix = [
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    "X",
    " ",
    "X",
    " ",
]

# TODO revoir algo en utilisant le tableau et non la matrice
def get_with_math_only(i, j):
    global compact_matrix
    tab_length = len(compact_matrix)
    n = int((tab_length + 6) / 5)
    if j in [0, math.floor(n / 2), n - 1]:
        return "X"

    else:
        if (j > 0 and j < math.floor(n / 2) and i == 0) or (
            j > math.floor(n / 2) and j < n - 1 and i == n - 1
        ):
            return "X"

        else:
            return " "


def get(i, j):
    global compact_matrix
    tab_length = len(compact_matrix)
    n = int((tab_length + 6) / 5)
    if j in [0, math.floor(n / 2), n - 1]:
        return compact_matrix[((n - 1) * (j // math.floor(n / 2))) + i]
    else:
        # TODO Ça ne marche pas
        if i == 0:
            return compact_matrix[((n - 1) * 3) + j - 3]
        elif i == n - 1:
            return compact_matrix[((n - 1) * 3) + (n - 3) + j - 3]


n = 5
matrix = [[" " for i in range(n)] for i in range(n)]

for j in range(n):
    for i in range(n):
        matrix[j][i] = get(i, j)

print(np.matrix(matrix))
