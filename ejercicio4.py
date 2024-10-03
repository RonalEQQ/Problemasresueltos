import matplotlib.pyplot as plt
import numpy as np
# Solicitudes por segundo
x_values = np.arange(10, 21)
U_values = 2 * x_values**2 + 10 * x_values  # Fórmula de uso de CPU

# Uso máximo de CPU
cpu_limit = 80
print(f"Uso de CPU para 10 solicitudes: {2 * 10**2 + 10 * 10}")

# Graficar
plt.plot(x_values, U_values, marker='o')
plt.axhline(y=cpu_limit, color='r', linestyle='--', label='Límite de CPU = 80%')
plt.title('Uso de CPU vs Solicitudes por segundo')
plt.xlabel('Solicitudes por segundo')
plt.ylabel('Uso de CPU (%)')
plt.legend()
plt.grid(True)
plt.show()
