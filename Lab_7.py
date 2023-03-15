# Вариант 5
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import csv
from matplotlib.animation import PillowWriter

# Задание 1
print("Задание 1")

# Перемножение стандартных списков
list1 = [random.random() for i in range(1000000)]
list2 = [random.random() for i in range(1000000)]

t1_start = time.perf_counter()
for i in range(len(list1)):
    list1[i] *= list2[i]
time1 = time.perf_counter() - t1_start

# Перемножение массивов NumPy
numpy_list1 = np.array(list1)
numpy_list2 = np.array(list2)

t2_start = time.perf_counter()
numpy_list_a = np.multiply(numpy_list1, numpy_list2)
time2 = time.perf_counter() - t2_start

print('Время умножения стандартных списков: ', time1)
print('Время умножения массивов NumPy:',  time2)


# Задание 2
time = []
engine_speed = []
idle_speed = []
with open('data1.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        time.append(float(row['Время']))
        engine_speed.append(float(row['Обороты двигателя (об/мин)']))
        idle_speed.append(float(row['Обороты холостого хода (об/мин)']))

time = np.array(time)
engine_speed = np.array(engine_speed)
idle_speed = np.array(idle_speed)

# Построение графиков, наложенных друг на друга
plt.title('Зависимость от времени оборотов двигателя \n и оборотов холостого хода')
plt.xlabel('Время')
plt.ylabel('Обороты двигателя (об/мин) \n и Обороты холостого хода (об/мин) в течении времени')
plt.plot(time, engine_speed, color='green')
plt.plot(time, idle_speed, color='red')
plt.show()

# Построение графика корелляции
plt.title('График корреляции')
plt.xlabel('Обороты двигателя (об/мин)')
plt.ylabel('Обороты холостого хода (об/мин)')
plt.scatter(engine_speed, idle_speed, color='green')
plt.show()


# Задание 3
xs = np.linspace(-1 * np.pi, np.pi, 50)
ys = np.cos(xs) * np.sin(xs)
zs = np.sin(xs)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, c='red')
plt.title('График формулы x∈(-п;п); y=sin(x)cos(x); z=sin(x)')
plt.show()


# Дополнительное задание
fig = plt.figure()
line, = plt.plot([], [])

plt.xlim(-10, 10)
plt.ylim(-np.pi/2, np.pi/2)

writer = PillowWriter(fps=25)
x_list = []
y_list = []
with writer.saving(fig, "sin_x.gif", 150):
    for x in np.linspace(-10, 10, 150):
        x_list.append(x)
        y_list.append(np.sin(x))
        line.set_data(x_list, y_list)
        writer.grab_frame()
