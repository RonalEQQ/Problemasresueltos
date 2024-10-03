import matplotlib.pyplot as plt
import numpy as np
# Número de puntos de datos procesados
x_values = np.arange(1, 11)
T_values = 5 * x_values + 2  # Fórmula de tiempo

# Máximo número de puntos de datos
max_x = (50 - 2) / 5
print(f"Máximo número de puntos de datos procesados: {int(max_x)}")

# Graficar
plt.plot(x_values, T_values, marker='o')
plt.axhline(y=50, color='r', linestyle='--', label='Límite de 50 segundos')
plt.title('Tiempo de procesamiento vs Puntos de datos')
plt.xlabel('Puntos de datos procesados')
plt.ylabel('Tiempo tomado (segundos)')
plt.legend()
plt.grid(True)
plt.show()
