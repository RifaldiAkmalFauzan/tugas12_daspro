from matematika import persegi
import matematika.lingkaran as lingkaran
from matematika.bangun_ruang.kubus import volume_kubus, luas_permukaan_kubus
from matematika.bangun_ruang import bola

sisi = 5
r = 7

print("Program Matematika Sederhana - Created by Rifaldi\n")
print("Luas Persegi:", persegi.luas_persegi(sisi))
print("Keliling Persegi:", persegi.keliling_persegi(sisi))

print("\nLuas Lingkaran:", round(lingkaran.luas_lingkaran(r), 2))
print("Keliling Lingkaran:", round(lingkaran.keliling_lingkaran(r), 2))

print("\nVolume Kubus:", volume_kubus(sisi))
print("Luas Permukaan Kubus:", luas_permukaan_kubus(sisi))

print("\nVolume Bola:", round(bola.volume_bola(r), 2))
print("Luas Permukaan Bola:", round(bola.luas_permukaan_bola(r), 2))