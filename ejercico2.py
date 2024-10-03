import matplotlib.pyplot as plt
import numpy as np

# Número de nodos
n = 20
# Solicitudes por nodo (máximo 20)
x_values = np.arange(1, 21)
total_requests = x_values * n

# Máximas solicitudes por nodo
max_requests_per_node = 400 / n
print(f"Máximas solicitudes por nodo: {max_requests_per_node} solicitudes/segundo")

# Graficar
plt.plot(x_values, total_requests)
plt.axhline(y=400, color='r', linestyle='--', label='Límite de 400 solicitudes')
plt.title('Solicitudes totales procesadas vs Solicitudes por nodo')
plt.xlabel('Solicitudes por nodo')
plt.ylabel('Solicitudes totales procesadas')
plt.legend()
plt.grid(True)
plt.show()

