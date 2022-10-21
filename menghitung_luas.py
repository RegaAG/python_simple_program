print("Menghitung Luas")
print("Powered by Rega")

print("="*50)

print("""
Ket :
1. Luas Persegi panjang
2. Luas Segitiga
3. Luas Lingkaran
""")

print("="*50)

a = int(input("pilih program : "))
print("")

if a == 1:
    print("Luas Persegi panjang")
    p = int(input("Panjang : "))
    l = int(input("Lebar : "))
    luas = p*l
    print("Luas Persegi panjang : ", luas, "cm")

elif a == 2:
    print("Luas Segitiga")
    alas = int(input("Alas : "))
    tinggi = int(input("Tinggi : "))
    luas = alas * tinggi * 1/2
    print("Luas Segitiga : ", luas)

elif a == 3:
    print("Luas Lingkaran")
    phi = 22/7
    r = int(input("Jari-jari : "))
    luas = phi * r * r
    print("Luas Lingkaran : ", luas, "cm")


else:
    print("Program tidak ada")
