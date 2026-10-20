import numpy as np
import scipy


def print_matrix(matrix):
    n, m = matrix.shape
    matrix_temp = matrix.reshape(n * m)
    matrix_temp = np.array([(i if i%1 > 1e-8 else int(i)) for i in matrix_temp], dtype=object)
    matrix = matrix_temp.reshape(n, m)

    if len(matrix.shape) == 2:
        print(*['\t'.join([str(j) for j in i]) for i in matrix], sep='\n')
    else:
        print(*[str(i) for i in matrix], sep='\t')


# 1
A = np.array([[3, -1.2, -8, 8], [21, -19, 0.5, 0], [7, 0, -4.9, -2], [1, -2, 13, 9]])
b = np.array([20, -8, 11, 3])

# 2
P, L, U = scipy.linalg.lu(A)
print("Матрица P:")
print_matrix(P)
print("Матрица L:")
print_matrix(L)
print("Матрица U:")
print_matrix(U)

# 3
det_A = np.prod(np.diag(L)) * np.prod(np.diag(U)) * np.linalg.det(np.linalg.inv(P))
print("Определитель A:")
print(det_A)

# 4
np.random.seed(0)

numbers1 = np.random.randint(0, 11, 100)
numbers2 = np.random.normal(5, 5/3, 100).astype(int)

# 5
print(f'Среднее для numbers1: {np.average(numbers1)}')
print(f'Среднее для numbers2: {np.average(numbers2)}')
print(f'Мода для numbers1: {scipy.stats.mode(numbers1).mode[0]}')
print(f'Мода для numbers2: {scipy.stats.mode(numbers2).mode[0]}')
print(f'Медиана для numbers1: {np.median(numbers1)}')
print(f'Медиана для numbers2: {np.median(numbers2)}')
print(f'Минимум для numbers1: {np.min(numbers1)}')
print(f'Минимум для numbers2: {np.min(numbers2)}')
print(f'Максимум для numbers1: {np.max(numbers1)}')
print(f'Максимум для numbers2: {np.max(numbers2)}')
print(f'Стандартное отклонение для numbers1: {np.std(numbers1)}')
print(f'Стандартное отклонение для numbers2: {np.std(numbers2)}')

# 6
def chi_hyp(numbers, name):
    bins = 10
    observed, bin_edges = np.histogram(numbers, bins=bins)
    expected = np.full(bins, len(numbers) / bins)
    chi, p_value = scipy.stats.chisquare(observed, expected)

    print(f"Хи-квадрат тест для {name}:")
    print(f"Хи-квадрат статистика: {chi}")
    print(f"p-value: {p_value}")
    print(f"Нулевая гипотеза отвергнута при alpha=0.05: {p_value < 0.05}")

chi_hyp(numbers1, 'numbers1')
chi_hyp(numbers2, 'numbers2')
