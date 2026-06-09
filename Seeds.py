import matplotlib.pyplot as plt
import numpy as np

lamda = [0.11, 0.12, 0.13, 0.14]
teta = [0.001, 0.002, 0.003, 0.004]
c = 0.002
gama = 0.00030

seeds = []

for i in range(len(lamda)):
    fila = []
    for j in range(len(teta)):
        fila.append((c/gama)*(lamda[i] / (teta[j] + c)))
    seeds.append(fila)

# Malla para la superficie
X, Y = np.meshgrid(teta, lamda)
Z = np.array(seeds)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Superficie
ax.plot_surface(X, Y, Z, alpha=0.7)

# Puntos
ax.scatter(X, Y, Z, marker='o', s=50)

ax.set_title('Seeds')
ax.set_xlabel('θ')
ax.set_ylabel('λ')
ax.set_zlabel('Valor')

plt.show()