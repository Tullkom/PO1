import numpy as np
import matplotlib.pyplot as plt

# 1
a, b = 0, 1
points = 10
x = np.linspace(a, b, points)
y = np.sin(np.sqrt(2 * x))

# 2
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = sin(sqrt(2x))')
plt.title('График функции y = sin(sqrt(2x))')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, color='black', alpha=0.25)
plt.show()

# 3
plt.figure(figsize=(8, 6))
plt.scatter(x, y, marker='o', c=[(0.1, 0.1, 0.2)])
plt.title('Точечный график функции y = sin(sqrt(2x))')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, color='black', alpha=0.25)
plt.show()

# 4
np.random.seed(0)
numbers1 = np.random.randint(0, 11, 100)
numbers2 = np.clip(np.random.normal(5, 5/3, 100), 0, 10).astype(int)

plt.figure(figsize=(8, 6))
plt.hist(numbers1, bins=10, color='blue')
plt.title('Случайное распределение')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(numbers2, bins=9, color='red')
plt.title('Нормальное распределение')
plt.show()

# 5
numbers3 = np.random.randint(1, 5, 50)
values, counts = np.unique(numbers3, return_counts=True)
labels = values.astype(str)
colors_list = ['red', 'green', 'blue', "yellow"]

plt.figure(figsize=(8, 6))
wedges, texts = plt.pie(counts, labels=labels, colors=colors_list)
plt.title('Круговая диаграмма частот')
plt.axis('equal')
plt.show()

plt.figure(figsize=(8, 6))
bars = plt.bar(labels, counts, color=colors_list)
plt.title('Столбчатая диаграмма частот')
plt.xlabel('Число')
plt.ylabel('Количество')
plt.show()

# 6
def func(vars):
    x1, x2 = vars
    return (x1 + 3)**3 + (x2 - 3)**2

resolution = 100
x_range = np.linspace(0, 10, resolution)
y_range = np.linspace(0, 10, resolution)
X, Y = np.meshgrid(x_range, y_range)

Z = np.zeros_like(X)
for i in range(resolution):
    for j in range(resolution):
        Z[i, j] = func((X[i, j], Y[i, j]))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, color='blue')

ax.set_title('3D график функции z = (x+3)^3 + (y-3)^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

# 7
def grid_plots():
    fig = plt.figure(figsize=(16, 12))
    
    fig.suptitle('Сетка графиков')
    
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(x, y, label='sin(sqrt(2x))')
    ax1.set_title('2. График функции y=sin(sqrt(2x))')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True, color='black', alpha=0.25)
    
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.scatter(x, y, marker='o', c=[(0.1, 0.1, 0.2)])
    ax2.set_title('3. Точечный график')
    ax2.set_facecolor('yellow')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.grid(True, color='black', alpha=0.25)
    
    ax3 = fig.add_subplot(2, 2, 3)
    wedges, texts = ax3.pie(counts, labels=labels, colors=colors_list)
    ax3.set_title('5. Круговая диаграмма')
    
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    ax4.plot_surface(X, Y, Z, alpha=0.5, color='blue')
    ax4.set_title('6. 3D график функции z = (x+3)^3 + (y-3)^2')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('z')

    return fig

styles = ['default', 'bmh', 'Solarize_Light2', 'ggplot']

for style in styles:
    with plt.style.context(style):
        fig = grid_plots()
        plt.show()
