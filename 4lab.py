   import numpy as np
import matplotlib.pyplot as plt

# 1
a, b = 0, 1
num_points = 10
x = np.linspace(a, b, num_points)
y = np.sin(np.sqrt(2 * x))

# 2
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = sin(sqrt(2x))')
plt.title('График функции y = sin(sqrt(2x))')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 3
plt.figure(figsize=(8, 6))
plt.scatter(x, y, marker='o', c=[(0.11, 0.12, 0.19)])

plt.title('Точечный график функции y = sin(sqrt(2x))')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True, which='both', color='black', alpha=0.25)
plt.show()

# 4
np.random.seed(0)
numbers1 = np.random.randint(0, 11, 100)
numbers2 = np.random.normal(5, 5/3, 100).astype(int)

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(numbers1, bins=10, alpha=0.5, color='blue', label='Равномерное')
ax.hist(numbers2, bins=9, alpha=0.5, color='red', label='Нормальное')

ax.set_title('Гистограммы выборок')
ax.legend(loc='upper right')
plt.show()

# 5
numbers3 = np.random.randint(1, 5, 50)
unique_values, counts = np.unique(numbers3, return_counts=True)
labels = unique_values.astype(str)
colors_list = ['#FF0000', '#00FF00', '#0000FF', "#FFFF00"]

plt.figure(figsize=(8, 6))
wedges, texts = plt.pie(counts, labels=labels, colors=colors_list)
plt.title('Круговая диаграмма частот')
plt.axis('equal')
plt.show()

plt.figure(figsize=(8, 6))
bars = plt.bar(labels, counts, color=colors_list, edgecolor='black')
plt.title('Столбчатая диаграмма частот')
plt.xlabel('Число')
plt.ylabel('Количество')
plt.show()

# 6
def func(vars):
    x1, x2 = vars
    return (x1 + 3)**3 + (x2 - 3)**2

resolution = 100
x_range = np.linspace(-5, 5, resolution)
y_range = np.linspace(-5, 5, resolution)
X1, X2 = np.meshgrid(x_range, y_range)

Z = np.zeros_like(X1)
for i in range(resolution):
    for j in range(resolution):
        Z[i, j] = func((X1[i, j], X2[i, j]))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1, X2, Z, cmap='viridis', edgecolor='none', alpha=0.8)

line_color = 'red'
for k in range(0, resolution, 10):
    ax.plot(X1[k, :], X2[k, :], Z[k, :], color=line_color, lw=2, label=f'Линия сечения {k}' if k==0 else "")

ax.set_title('3D график функции z = (x+3)^3 + (y-3)^2')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
plt.show()

# 7
def draw_grid_of_plots():
    fig = plt.figure(figsize=(12, 10))
    
    fig.suptitle('Сетка графиков')
    
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(x, y, label='sin(sqrt(2x))')
    ax1.set_title('2. График функции y=sin(sqrt(2x))')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.scatter(x, y, marker='o', c=[(0.11, 0.12, 0.19)], s=20, label='Точки', edgecolors='black', linewidths=0.5)
    ax2.set_title('3. Точечный график', fontsize=10)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.legend()
    ax2.grid(True, linestyle='-', color='gray', alpha=0.6)
    
    ax3 = fig.add_subplot(2, 2, 3)
    data_local = np.random.randint(1, 5, 50)
    u_vals, c_vals = np.unique(data_local, return_counts=True)
    local_labels = u_vals.astype(str)
    local_colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00'][:len(c_vals)]
    wedges, texts = ax3.pie(c_vals, labels=local_labels, colors=local_colors)
    ax3.set_title('5. Круговая диаграмма')
    ax3.patch.set_facecolor('#F0F0F0') 
    
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    ax4.set_title('6. 3D График', fontsize=10)
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('z')
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    return fig

styles = ['default', 'bmh', 'dark_background', 'ggplot'] 

for style in styles:
    with plt.style.context(style):
        fig = draw_grid_of_plots()
        plt.show()