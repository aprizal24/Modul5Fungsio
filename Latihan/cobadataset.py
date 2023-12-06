import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Membuat dataset sederhana
np.random.seed(42)
data = {
    'Tanggal': pd.date_range(start='2023-04-01', end='2023-04-10'),
    'Penjualan': np.random.randint(50, 100, size=10)
}

dataset = pd.DataFrame(data)

# Plotting dataset
plt.figure(figsize=(15,5))
plt.plot(dataset['Tanggal'], dataset['Penjualan'], marker='o')
plt.title('Grafik Penjualan Harian', loc='center', fontsize=20, color='blue')
plt.xlabel('Tanggal', fontsize=15)
plt.ylabel('Penjualan', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.show()
