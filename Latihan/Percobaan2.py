import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([50, 60, 70, 80, 90, 100])
ypoints = np.array ([3, 10, 15, 3, 8, 6])

plt.figure(figsize=(15,5))
plt.plot(xpoints, ypoints, color='red', marker='o')
plt.title('Grafik Nilai Mahasiswa', fontsize=15, color='blue')
plt.xlabel('Nilai Mahasiswa', fontsize=10)
plt.ylabel('Jumlah Mahasiswa', fontsize=10)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt. show()