#Побудуйте графік функції. Оберіть суцільний тип лінії, задайте колір та товщину графіку
# та позначте осі, виведіть назву графіка на екран, вставте легенду.
# Використайте бібліотеку Matplotlib.
#Y(x)=5*cos(10*x)*sin(3*x)/(x^(1/2)), x=[0...5]

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001, 5, 100) # починаю з 0.001, бо у формулі буде ділення на нуль якщо почати з 0
y = 5*np.cos(10*x)*np.sin(3*x)/(x**(1/2))

plt.plot(x, y, label='Y(x)=5*cos(10*x)*sin(3*x)/(x^(1/2))', color= 'g',linewidth = 5)
plt.title('Завдання 1', fontsize=15)
plt.xlabel('x', fontsize=12, color='r') # позначення вісі абсцис
plt.ylabel('y', fontsize=12, color='r') # позначення вісі ординат
plt.legend()
plt.grid()
plt.show()