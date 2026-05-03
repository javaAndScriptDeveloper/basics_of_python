import matplotlib.pyplot as plt

# Твої розраховані дані
x_lg_T = [3.12, 3.18, 3.22, 3.29, 3.32, 3.33, 3.36]
y_lg_W_aT = [1.15, 1.38, 1.58, 1.72, 1.86, 1.97, 2.09]

# Побудова графіка
plt.figure(figsize=(8, 5))
plt.plot(x_lg_T, y_lg_W_aT, marker='o', linestyle='-', color='#2ca02c', linewidth=2, markersize=6)

# Оформлення за вимогами до лабораторних
plt.title('Графік залежності lg(W/a_T) від lg T')
plt.xlabel('lg T')
plt.ylabel('lg(W/a_T)')
plt.grid(True, linestyle='--', alpha=0.7)

# Збереження та показ
plt.savefig('lab3_08_graph.png', dpi=300, bbox_inches='tight')
plt.show()