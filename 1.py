import numpy as np


class MatrixLab():
    def __init__(self):
        self.A = None
        self.B = None
        self.my_array = None
        np.random.seed(404)

    def gen_array(self):
        my_array = np.arange(10, 70, 2)
        print('1. Созданный массив:')
        print(*my_array, sep=' ')
        self.my_array = my_array

    def gen_matrix_A(self):
        A = self.my_array.reshape(6, 5)
        A = np.transpose(A)
        print('2. Размерность сформированной матрицы:')
        print(A.shape)
        self.A = A

    def change_matrix(self):
        A = self.A*2.5 - 5
        print('3. Полученная матрица:')
        print(A)
        print('Её минимальный элемент:', A.min())
        self.A = A

    def gen_matrix_B(self):
        B = np.random.uniform(0, 10, (6, 3))
        print('4. Полученная матрица:')
        print(B)
        print('Размерность сформированной матрицы:', B.shape)
        self.B = B

    def sum_vectors(self):
        sum_A = self.A.sum(axis=1)
        sum_B = self.B.sum(axis=0)
        print('5. Вектор сумм по строкам матрицы А:')
        print(sum_A)
        print('Его размерность:', sum_A.shape)
        print('Вектор сумм по столбцам матрицы B:')
        print(sum_B)
        print('Его размерность:', sum_B.shape)

    def multiply_matrix(self):
        C = np.matmul(self.A, self.B)
        print('6. Матричное произведение A*B:')
        print(C)
        print('Размерность сформированной матрицы:', C.shape)

    def matrix_to_square(self):
        A = np.delete(self.A, 2, axis=1)
        C = np.random.uniform(10, 20, (6, 3))
        B = np.concat((self.B, C), axis=1)
        print('7. Матрица А, приведённая к квадратному виду:')
        print(A)
        print('Размерность сформированной матрицы:', A.shape)
        print('Матрица B, приведённая к квадратному виду:')
        print(B)
        print('Размерность сформированной матрицы:', B.shape)
        self.A = A
        self.B = B

    def det_and_inv(self):
        det_A = np.linalg.det(self.A)
        print('8. Определитель матрицы A:', det_A)
        det_B = np.linalg.det(self.B)
        print('Определитель матрицы B:', det_B)
        try:
            inv_A = np.linalg.inv(self.A)
            print('Обратная матрица для A:')
            print(inv_A)
        except Exception as e:
            print('Обратная матрица для A не существует')
            print(e)
        try:
            inv_B = np.linalg.inv(self.B)
            print('Обратная матрица для B:')
            print(inv_B)
        except Exception as e:
            print('Обратная матрица для B не существует')
            print(e)

    def pow_matrix(self):
        print('9. Матрица А, возведённая в 6 степень:')
        Apow6 = np.linalg.matrix_power(self.A, 6)
        print(Apow6)
        print('Матрица B, возведённая в 14 степень:')
        Bpow14 = np.linalg.matrix_power(self.B, 14)
        print(Bpow14)
        self.A = Apow6
        self.B = Bpow14

    def additional_analysis(self):
        print('11. Дополнительный анализ матриц')
        print('Ранг матрицы А:', np.linalg.matrix_rank(self.A))
        print('Ранг матрицы B:', np.linalg.matrix_rank(self.B))
        print('Среднее значение в матрице А:', np.average(self.A))
        print('Среднее значение в матрице B:', np.average(self.B))
        print('Ковариационная матрица для A:')
        print(np.cov(self.A))
        print('Ковариационная матрица для B:')
        print(np.cov(self.B))
        i, j = np.unravel_index(np.argmax(self.A), self.A.shape)
        print('Индексы строки и столбца максимального элемента A:', i, j)
        print('B как одномерный вектор:')
        print(self.B.flatten())
        print('Его размер:', self.B.flatten().shape)

    def save_to_txt(self):
        np.savetxt('A.csv', self.A, delimiter=',')
        np.savetxt('B.csv', self.B, delimiter=',')

    def load_from_txt(self, path):
        return np.loadtxt(path, delimiter=',')

    def save_load_test(self):
        self.save_to_txt()
        delta_A = (self.A - self.load_from_txt('A.csv')).max()
        delta_B = (self.B - self.load_from_txt('B.csv')).max()
        print('12. Сохранение и загрузка матриц')
        print('Разница A:', delta_A)
        print('Разница B:', delta_B)

    def linear_eq(self):
        print("10. СЛАУ 3 вариант")
        A = [[3, -1.2, -8, 8], [21, -19, 0.5, 0], [7, 0, -4.9, -2], [1, -2, 13, 9]]
        print("Коэффициенты:")
        print(A)
        b = [20, -8, 11, 3]
        print('Вектор правых частей:', b)
        x = np.linalg.solve(A, b)
        print('Решение СЛАУ:', x)
        residual = np.matmul(A, x) - b
        print('Невязка:', residual)
        if np.allclose(residual, 0):
            print('Невязка близка к нулю')
        else:
            print('Невязка слишком большая')


def run():
    MatLab = MatrixLab()
    MatLab.gen_array()
    MatLab.gen_matrix_A()
    MatLab.change_matrix()
    MatLab.gen_matrix_B()
    MatLab.sum_vectors()
    MatLab.multiply_matrix()
    MatLab.matrix_to_square()
    MatLab.det_and_inv()
    MatLab.pow_matrix()
    MatLab.linear_eq()
    MatLab.additional_analysis()
    MatLab.save_load_test()


if __name__ == "__main__":
    run()
