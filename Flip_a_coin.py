import random

print("Ket.\n 'a' untuk angka, dan 'g' untuk gambar")
pemain = input ("masukkan pilihanmu \n> ").lower()

bot = random.choice(['g', 'a'])

print("pilihanmu : "+pemain)
print("Komputer : "+bot)

if pemain == bot:
    print("Selamat Tebakanmu Benar ")

elif (pemain == "a" and bot == "g") or (pemain == "g" and bot == "a"):
    print("Tebakanmu Salah")
