import numpy as np

matrix = np.array([
    [3, 7, 2, 9],
    [8, 3, 6, 7],
    [4, 8, 3, 5],
    [9, 6, 5, 4]
])
weights = np.array([8, 9, 6, 7])
criteria_values = np.dot(matrix, weights)
print(criteria_values)
position = np.argmax(criteria_values)
print(position)
print(f"ОПР найкраще укласти договір з адвокатом під номером: {position+1} з функцією корисності {criteria_values[position]}")
