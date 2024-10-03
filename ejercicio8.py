import matplotlib.pyplot as plt
import numpy as np

# Tamaño de lote
x_values = np.arange(1, 21)

# Fórmula de consumo de energía
E_values = np.piecewise(x_values, [x_values <= 10, x_values > 10], 
                        [lambda x: x, lambda x: x * (1 + 0.1 * (x - 10))])

total_energy = x_values * E_values

# Máximo tamaño de lote
max_batch_size = 14
print(f"Tamaño de lote máximo: {max_batch_size}")

# Graficar
plt.plot(x_values, total_energy, marker='o')
plt.axhline(y=200, color='r', linestyle='--', label='Límite de 200 unidades')
plt.title('Consumo de energía vs Tamaño de lote')
plt.xlabel('Tamaño de lote')
plt.ylabel('Consumo total de energía')
plt.legend()
plt.grid(True)
plt.show()
