import math
luas = lambda r: math.pi * r ** 2

#Contoh Penggunaan
radius = 6
print("Jadi Luas Lingkaran: ", luas(radius))
print (" ")

#Kode Input dari Pengguna
floatinput = float(input("Masukkan jari-jari lingkaran: "))
luaslingkaran = luas(floatinput)
print("Luas lingkaran dengan jari-jari", floatinput, "adalah:", luaslingkaran)