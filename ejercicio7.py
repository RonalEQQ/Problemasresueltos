import matplotlib.pyplot as plt
import numpy as np

# Trabajos por segundo
x_values = np.arange(5, 21)
T_values = 100 / x_values + 2 * x_values  # Fórmula de tiempo de respuesta

# Trabajos por segundo óptimos
x_optimal = np.sqrt(50)
print(f"Trabajos procesados por segundo óptimos: {x_optimal:.2f}")

# Graficar
plt.plot(x_values, T_values, marker='o')
plt.title('Tiempo de respuesta vs Trabajos procesados por segundo')
plt.xlabel('Trabajos por segundo')
plt.ylabel('Tiempo de respuesta (ms)')
plt.grid(True)
plt.show()
