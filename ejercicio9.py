import matplotlib.pyplot as plt
import numpy as np

# Rango de almacenamiento (TB)
x_values = np.arange(0, 91)
C_values = 50 + 5 * x_values  # Fórmula de costo

# Máximo almacenamiento
max_storage = (500 - 50) / 5
print(f"Almacenamiento máximo sin exceder el presupuesto: {int(max_storage)} TB")

# Graficar
plt.plot(x_values, C_values, marker='o')
plt.axhline(y=500, color='r', linestyle='--', label='Límite de presupuesto = 500')
plt.title('Costo de almacenamiento vs Cantidad de almacenamiento')
plt.xlabel('Almacenamiento (TB)')
plt.ylabel('Costo (USD)')
plt.legend()
plt.grid(True)
plt.show()
