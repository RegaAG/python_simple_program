print("="*25)
print("SELAMAT DATANG DI GAME TEBAK ASAL")
print("="*25)

print("PILIH KATEGORINYA")
print("1. Mudah")
print("2. Sedang")
print("3. Sulit")
print("_"*25)

pilih = int(input("Mau pilih kategori yang mana nih? \n1, 2, atau 3 : "))

if pilih == 1:
    print("="*25)
    print("KATEGORI MUDAH")
    print("="*25)

    tebakan = input("Siapakah grup band yang ga pernah memihak ? ")

    if tebakan == 'netral':
        print("Tebakan kamu benar")
    else:
        print("Tebakan kamu salah, jawabannya adalah Netral")

elif pilih == 2:
    print("="*25)
    print("KATEGORI SEDANG")
    print("="*25)

    tebakan = input("Bidadari-bidadari, kalo tanpa dada jadi apa? ")

    if tebakan == 'biri biri':
        print("Tebakan kamu benar, berarti pikiran kamu ga ngeres")
    else:
        print("Tebakan kamu Salah, jawabannya biri biri. Kamu tadi mikir yang nggak-nggak yah?")

elif pilih == 3:
    print("="*25)
    print("KATEGORI SULIT")
    print("="*25)

    tebakan = input("Siapakah mantan dari penulis artikel ini ?")

    if tebakan == 'Maaf Kurang Beruntung':
        print("Tebakan kamu Bener. Kok kamu tahu sih ?")

    else:
        print("Tebakan kamu Salah, coba deh tanya pacar kamu. Siapa tau dia mantan si penulis wkwkwk")

else:
    print("Erorr")
