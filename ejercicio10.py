import matplotlib.pyplot as plt
import numpy as np

# Número de mensajes por segundo
x_values = np.arange(1, 41)
L_values = 100 - 2 * x_values  # Fórmula de latencia

# Máximo de mensajes antes de que la latencia caiga por debajo de 20ms
max_messages = (100 - 20) / 2
print(f"Número máximo de mensajes por segundo: {int(max_messages)}")

# Graficar
plt.plot(x_values, L_values, marker='o')
plt.axhline(y=20, color='r', linestyle='--', label='Límite de latencia = 20ms')
plt.title('Latencia vs Número de Mensajes')
plt.xlabel('Mensajes por Segundo')
plt.ylabel('Latencia (ms)')
plt.legend()
plt.grid(True)
plt.show()
