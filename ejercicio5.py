import matplotlib.pyplot as plt
import numpy as np

# Rango de tamaño de lote
x_values = np.arange(16, 129)
T_values = 1000 / x_values + 0.1 * x_values  # Fórmula de tiempo de entrenamiento

# Tiempo mínimo de entrenamiento
x_optimal = 100
T_optimal = 1000 / x_optimal + 0.1 * x_optimal
print(f"Tamaño de lote óptimo: {x_optimal}")
print(f"Tiempo mínimo de entrenamiento: {T_optimal} segundos")

# Graficar
plt.plot(x_values, T_values, marker='o')
plt.title('Tiempo de entrenamiento vs Tamaño de lote')
plt.xlabel('Tamaño de lote')
plt.ylabel('Tiempo de entrenamiento (segundos)')
plt.grid(True)
plt.show()
