import matplotlib.pyplot as plt
import numpy as np

# Диаграмма количеств фруктов в соответсвии
fruits = ["apple", "peach", "orange", "bannana", "melon"]
counts = [34, 25, 43, 31, 17]

plt.bar(fruits, counts)
plt.title("FRUETS")
plt.xlabel("Fruit")
plt.ylabel("Count")

plt.show()