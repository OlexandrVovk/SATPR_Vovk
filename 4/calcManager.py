import numpy as np

class calcManager:
    def __init__(self):
        pass

    def pessimistic_criterion(self, matrix):
        min_values = np.min(matrix, axis=1)
        result = np.where(min_values == np.min(matrix))[0]
        print("За критерієм песимізму: ", result+1)

    def optimistic_criterion(self, matrix):
        min_values = np.min(matrix, axis=1)
        optimal_alternative = np.argmax(min_values)
        print("За критерієм оптимізму: ", optimal_alternative+1)

    def hurwicz_criterion(self, matrix, alpha):
        min_values = np.min(matrix, axis=1)
        max_values = np.max(matrix, axis=1)
        hurwicz_values = alpha * min_values + (1 - alpha) * max_values
        optimal_alternative = np.argmax(hurwicz_values)
        print("За критерієм Гурвіца: ", optimal_alternative+1)

    def laplace_criterion(self, matrix):
        laplace_values = np.mean(matrix, axis=1)
        optimal_alternative = np.argmax(laplace_values)
        print("За критерієм Лапласа: ", optimal_alternative + 1)

    def bayes_laplace_criterion(self, matrix, probabilities):
        bayes_laplace_values = np.dot(matrix, probabilities)
        print("За критерієм Баєса-Лапласа: ", np.argmax(bayes_laplace_values) + 1)


    def hodges_lehmann_criterion(self, matrix, probabilities, alpha):
        min_values = np.min(matrix, axis=1)
        hurwicz_values = (1 - alpha) * min_values + np.dot(matrix, probabilities) * alpha
        optimal_alternative = np.argmax(hurwicz_values)
        print("За критерієм Ходжа-Лемана: ", optimal_alternative + 1)

    def normalize_matrix(self,matrix, minimize_criteria_indices):
        weights = np.ones(matrix.shape[1])
        for idx in minimize_criteria_indices:
            weights[idx] = -1

        max_values = np.max(matrix, axis=0)
        min_values = np.min(matrix, axis=0)
        normalized_matrix = (matrix - min_values) / (max_values - min_values) * weights
        normalized_matrix[:, minimize_criteria_indices] = np.flip(normalized_matrix[:, minimize_criteria_indices]) * -1
        return normalized_matrix
