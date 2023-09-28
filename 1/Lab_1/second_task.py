import numpy as np

matrix = np.array([
    [85, 30, 22, 0.65, 6],
    [60, 20, 10, 0.6, 7],
    [30, 12, 5, 0.45, 5],
    [75, 24, 13, 0.7, 8],
    [40, 15, 7, 0.55, 7]
])
weights = np.array([7, 5, 6, 8, 6])
def normalize_matrix(matrix):
    if not isinstance(matrix, np.ndarray):
        print("type mismatch")
        quit()

    if len(matrix) != 5:
        print("invalid matrix")
        quit()

    for row in matrix:
        if not isinstance(row, np.ndarray) or len(row) != 5:
            print("invalid matrix")
            quit()

    min_values = np.min(matrix, axis=0)
    max_values = np.max(matrix, axis=0)
    first_normalized_column = (matrix[:, 0] - min_values[0]) / (max_values[0] - min_values[0])

    min_value = np.min(matrix[:, 1])
    max_value = np.max(matrix[:, 1])
    second_normalized_column = (max_value - matrix[:, 1]) / (max_value - min_value)

    min_value = np.min(matrix[:, 2])
    max_value = np.max(matrix[:, 2])
    third_normalized_column = (matrix[:, 2] - min_value) / (max_value - min_value)

    min_value = np.min(matrix[:, 3])
    max_value = np.max(matrix[:, 3])
    fourth_normalized_column= (matrix[:, 3] - min_value) / (max_value - min_value)

    min_value = np.min(matrix[:, 4])
    max_value = np.max(matrix[:, 4])
    last_normalized_column = (matrix[:, 4] - min_value) / (max_value - min_value)
    return np.column_stack((first_normalized_column,
                            second_normalized_column,
                            third_normalized_column,
                            fourth_normalized_column,
                            last_normalized_column))
result_matrix = np.dot(normalize_matrix(matrix), weights)
print(result_matrix)
position = np.argmax(result_matrix)
print(f"Директору найкраще найняти юриста під номером: {position+1} з функцією корисності {result_matrix[position]}")

