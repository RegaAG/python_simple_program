print("-"*25)
print("PERPUSTAKAAN SEDERHANA")
print("-"*25)

print("""
Kode   |   Judul     |   Tahun   |   Harga
Buku   |   Buku      |   Terbit  |   Buku
------------------------------
1     |   Spiderman  |   2021    |   3000/minggu
2     |   Venom      |   2018    |   5500/minggu
3     |   Marvel     |   2020    |   4500/minggu
4     |   Batman     |   2015    |   2500/minggu
5     |   Superman   |   2019    |   5000/minggu
------------------------------
""")

total = 0
buku = []
harga = []

pinjaman = int(input("Berapa lama pinjaman buku [minggu] : "))
while True:
    kode_buku = int(input("Masukan kode buku : "))
    if kode_buku == 1:
        buku.append('Spiderman')
        harga.append(3000)
        total += 3000 * pinjaman
    elif kode_buku == 2:
        buku.append('Venom')
        harga.append('5500')
        total += 5500 * pinjaman
    elif kode_buku == 3:
        buku.append('Marvel')
        harga.append(4500)
        total += 4500 * pinjaman
    elif kode_buku == 4:
        buku.append('Batman')
        harga.append(2500)
        total += 2500 * pinjaman
    elif kode_buku == 5:
        buku.append('Superman')
        harga.append(5000)
        total += 5000 * pinjaman
    else:
        print("Kode tidak valid")

    lanjut = input("Ingin menambah buku pinjaman (y/t) : ")
    if lanjut == 't':
        print()
        break


print(f"Anda akan meminjam buku {buku}")
print(f"Dengan harga dikali {pinjaman} minggu")
print(f"Total {total}")

uang = int(input("Masukan uang anda : "))
if uang >= total:
    kembalian = uang - total
    print(f"Kembalian anda {kembalian}, Terima kasih")

else:
    print("Uang anda tidak cukup")
