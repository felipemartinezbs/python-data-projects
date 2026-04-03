import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
ventas = pd.read_csv("ventas.csv")

# Total de ventas
total_ventas = ventas["ventas"].sum()

# Ventas por producto
ventas_producto = ventas.groupby("producto")["ventas"].sum()

# Ventas por región
ventas_region = ventas.groupby("region")["ventas"].sum()

print("===== SALES REPORT =====")
print("Total ventas:", total_ventas)

print("\nVentas por producto:")
print(ventas_producto)

print("\nVentas por región:")
print(ventas_region)

# Exportar reportes
ventas_producto.to_csv("ventas_por_producto.csv")
ventas_region.to_csv("ventas_por_region.csv")

# Crear gráfico
ventas_producto.plot(kind="bar")

plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.tight_layout()

# Guardar gráfico
plt.savefig("grafico_ventas.png")

print("\nReportes y gráfico generados correctamente.")