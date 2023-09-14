import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)  #Функция numpy.linspace() в Python используется для генерации последовательности чисел в линейном пространстве с одинаковым размером шага.

def sigmoid(alpha):
    return 1 / ( 1 + np.exp(- alpha * x) )

def main():
    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )

    plt.plot(x, sigmoid(0.5), 'ro-')
    plt.plot(x, sigmoid(1.0), 'go-')
    plt.plot(x, sigmoid(2.0), 'bo-')

    plt.legend(['A = 0.5', 'A = 1.0', 'A = 2.0'], loc = 'upper left')

    fig.savefig('sigmoid.png')
    
main()