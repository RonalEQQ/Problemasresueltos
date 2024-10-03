import matplotlib.pyplot as plt
import numpy as np

# Número de lotes y datos de memoria
n_values = np.arange(1, 9)
x_5_batches = 204  # Memoria máxima por lote para 5 lotes
x_8_batches = 128  # Memoria máxima por lote para 8 lotes

# Datos procesados
D_values = [5 * x_5_batches if n <= 5 else 5 * x_8_batches + 0.8 * x_8_batches * (n - 5) for n in n_values]

# Calcular resultados
D_5_batches = 5 * x_5_batches
D_8_batches = 5 * x_8_batches + 0.8 * x_8_batches * 3

print(f"Máximo de datos procesados con 5 lotes: {D_5_batches} MB")
print(f"Máximo de datos procesados con 8 lotes: {D_8_batches} MB")

# Graficar
plt.plot(n_values, D_values, marker='o')
plt.title('Datos procesados vs Número de lotes')
plt.xlabel('Número de lotes')
plt.ylabel('Datos procesados (MB)')
plt.grid(True)
plt.show()

