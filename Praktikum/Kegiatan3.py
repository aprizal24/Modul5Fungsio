import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# TODO 1: Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def hitung_frekuensi(tinggi_badan, interval_size):
    frekuensi = {}
    for tinggi in tinggi_badan:
        interval = tinggi // interval_size * interval_size
        if interval in frekuensi:
            frekuensi[interval] += 1
        else:
            frekuensi[interval] = 1
    return frekuensi

# TODO 2: Fungsi untuk menghitung frekuensi tinggi badan dalam interval
def plot_histogram_kurva_pdf(tinggi_badan, interval_size):
    frekuensi = hitung_frekuensi(tinggi_badan, interval_size)

    # TODO 3: Visualisasi data dalam bentuk histogram
    plt.figure(figsize=(7.5, 5))
    plt.hist(tinggi_badan, bins=range(150, 190 + interval_size, interval_size), label='Data')
    plt.title('Histogram Tinggi Badan')
    plt.xlabel('Interval Tinggi badan')
    plt.ylabel('Frekuensi')

    # TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
    mean, std = np.mean(tinggi_badan), np.std(tinggi_badan)
    x = np.linspace(155, 185)
    p = norm.pdf(x, mean, std) * len(tinggi_badan) * interval_size
    plt.plot(x, p, linewidth=2, color='red', label='Kurva PDF (Normal Distribution')

    # Menambahkan legenda
    plt.legend()
    plt.show()

# Menjalankan program
plot_histogram_kurva_pdf(tinggi_badan, interval_size)
