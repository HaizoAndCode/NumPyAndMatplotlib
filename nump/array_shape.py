import numpy as np
grid = np.arange(1, 10).reshape((3, 3))  # массив должен изменять форму так, чтобы он соответствовал размеру
# reshape((3, 3)) создает форму 3x3 для данного массива
print("Массив формой 3х3")
print(grid)

print("Для сравнения:")
grid1 = np.arange(1, 10)
print(grid1)

print()

# одномерный массив в двумерную матрицу-строку:
# методом reshape:
x = np.array([1, 2, 3])
x.reshape((1, 3))
print("с помощью reshape:")
print(x)

# но лучше использовать ключевое слово newaxis:
x[np.newaxis, :]
print("используя newaxis:")
print(x)

print()

# в матрицу-столбец:
print("Используя reshape:")
print(x.reshape((3, 1)))  # первый индекс количество строк, второй столбцов
print("Используя newaxis")
print(x[:, np.newaxis])
