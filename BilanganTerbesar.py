satu = int(input("Masukan bilangan ke-1 : "))
dua = int(input("Masukan bilangan ke-2 : "))
tiga = int(input("Masukan bilangan ke-3 : "))
print(f""*15)
if (satu > dua and satu > tiga):
    print(f"Bilangan terbesar adalah {satu}")
    if (satu >= 0):
        print(f"Bilangan Positif")
    else:
        print(f"Bilangan Negatif")

elif (dua > satu and dua > tiga):
    print(f"Bilangan terbesar adalah {dua}")
    if (dua >= 0):
        print(f"Bilangan Positif")
    else:
        print(f"Bilangan Negatif")

elif (tiga > satu and tiga > dua):
    print(f"Bilangan terbesar adalah {tiga}")
    if (tiga >= 0):
        print(f"Bilangan Positif")
    else:
        print(f"Bilangan Negatif")