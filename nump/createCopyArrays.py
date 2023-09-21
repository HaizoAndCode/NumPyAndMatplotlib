import numpy as np

# создали массив:
x = np.random.randint(10, size=(3, 4))
print(x)
print()

# копия подмассива x:
x_sub_copy = x[:2, :2].copy()
print(x_sub_copy)
print()

# copy() не влияет на главный массив, лишь создает его корию, изменения которого не влияют на сам массив:
x_sub_copy[0, 0] = 99
print(x_sub_copy)
print()

# замена элемента подмассива может изменить массив:
print("Начало замены элемента с помощью подмассива.") 
print("Сам массив: ")
print(x)
print()
print("Подмассив: ")
sub_x = x[:2, :2]
print(sub_x)
print()
print("Процесс замены:")
sub_x[0, 0] = 99
print(sub_x)
print()
print("итог изменений:")
print(x)
