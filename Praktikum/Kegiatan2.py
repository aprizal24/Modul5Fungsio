import matplotlib.pyplot as plt
import numpy as np

# Data transaksi
data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# Todo 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
data_array = np.array(data_transaksi)
nama_produk = data_array[:, 0]
harga_produk = data_array[:, 1].astype(int)
jumlah_terjual = data_array[:, 2].astype(int)

# Todo 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.scatter(harga_produk, jumlah_terjual, color='skyblue')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Produk Terjual')
# Todo 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = list(map(lambda item: item[1] * item[2], data_transaksi))


# Todo 4: Tambahkan bar chart untuk menyajikan pendapatan produk
plt.subplot(1, 2, 2)
plt.bar(nama_produk, pendapatan_produk, color='skyblue')
plt.xlabel('Produk')
plt.ylabel('Pendapatan Produk')
plt.title('Pendapatan Produk')

# Menampilkan kedua gambar terpisah
plt.tight_layout()
plt.show()
