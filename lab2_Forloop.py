# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini

# #variabel nilai awal = 100
nilai_awal = 100
# #variabel nilai akhir = 0
nilai_akhir = 0
# #variabel selang = -2
selang = -2
# #melakukan proses perulangan variabel i
for i in range(nilai_awal, nilai_akhir, selang):
#   #mencetak pesan/hasil dari perulangan variabel i
  print(i, end=' ')
#
print()
# #memberi jarak
#
# # SOAL 2 - Menghitung rata-rata
# # Tuliskan program untuk Soal 2 di bawah ini
#
# # variable yang menyimpan dan meminta masukan pengguna
n = eval(input("masukkan berapa bilangan :"))
# # variabel jumlah
jumlah = 0
# #proses perulangan yang diminta cetak oleh variabel n
for i in range(n):
#   # variabel yang menyimpan dan meminta masukan pengguna
    a = eval(input("masukkan bilangan:" ))
#   #variabel yang menghitung penjumlahan
    jumlah = jumlah+a
# #mencetak pesan/hasil dari penjumlahan
print("jumlah:", jumlah)
# #mencetak pesan/hasil dari penjumlahan ke nilai rata-rata
print("hasil rata-rata: ", jumlah/n)
#
# #memberi jarak
print()

# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini

# variable yang menyimpan dan meminta masukan pengguna
k = eval(input("Masukkan sebuah bilangan bulat:"))
#proses perulangan yang diminta cetak oleh variabel k
for q in range (k):
  #proses perulangan yang diminta cetak oleh variabel k
    for j in range(k):
      #mencetak pesan/hasil menjadi # sebuah persegi
        print('#', end='')
    # membuat/mencetak hasil menjadi kebawah
    print()