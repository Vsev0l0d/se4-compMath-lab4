from matrix import Matrix


def solve(matrix: Matrix, decimals: float):
    precision = 10 ** (-decimals)
    x_vector = [0] * matrix.size

    if not matrix.diagonally_dominant:
        if not matrix.make_diagonally_dominant():
            return None

    c_matrix = []
    for row in range(matrix.size):
        a_ii = matrix.coefficients[row][row]
        row_vector = []
        for column in range(matrix.size):
            c = -matrix.coefficients[row][column] / a_ii if row != column else 0
            row_vector.append(c)
        c_matrix.append(row_vector)

    error_vector = [1] * len(x_vector)
    while max(error_vector) > precision:
        for i in range(len(x_vector)):
            a = matrix.coefficients[i][i]
            b = matrix.b[i]
            cx_array_sum = 0
            for j in range(len(x_vector)):
                cx_array_sum += c_matrix[i][j] * x_vector[j]

            prev = x_vector[i]
            x_vector[i] = cx_array_sum + b / a
            error_vector[i] = abs(x_vector[i] - prev)

    return x_vector
