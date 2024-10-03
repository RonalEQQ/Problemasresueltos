import matplotlib.pyplot as plt
import numpy as np

# Rango de archivos
n_values = np.arange(1, 51)
x = 20  # Ancho de banda por archivo

# Fórmula de ancho de banda
A_values = np.piecewise(n_values, [n_values <= 30, n_values > 30], 
                        [lambda n: 1000, lambda n: 1000 * (1.5 - 0.05 * n)])

# Ancho de banda utilizado
bandwidth_used = n_values * x

# Máximo número de archivos transmitidos
max_files = 35
print(f"Máximo número de archivos transmitidos sin exceder el ancho de banda: {max_files}")

# Graficar
plt.plot(n_values, bandwidth_used, label='Ancho de banda usado (n * 20 Mbps)')
plt.plot(n_values, A_values, label='Ancho de banda disponible', linestyle='--')
plt.axvline(x=30, color='r', linestyle='--', label='Penalización desde n=30')
plt.title('Ancho de banda vs Número de archivos')
plt.xlabel('Número de archivos')
plt.ylabel('Ancho de banda (Mbps)')
plt.legend()
plt.grid(True)
plt.show()

