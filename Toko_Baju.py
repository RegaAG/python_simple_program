print("-"*25)
print("TOKO BAJU")
print("-"*25)

harga_baju_ukuran_s = float(input("Masukan harga baju ukuran S : "))

harga_baju_ukuran_l = harga_baju_ukuran_s * 1.1
harga_baju_ukuran_xl = harga_baju_ukuran_s * 1.5
harga_baju_ukuran_xxl = harga_baju_ukuran_s * 1.7

print("-"*25)
print(f"Harga baju ukuran S Rp.{harga_baju_ukuran_s:,}")
print(f"Harga baju ukuran L Rp.{harga_baju_ukuran_l:,}")
print(f"Harga baju ukuran XL Rp.{harga_baju_ukuran_xl:,}")
print(f"Harga baju ukuran XXL Rp.{harga_baju_ukuran_xxl:,}")
print("-"*25)

jumlah = 0
barang = []


while True:
    ukuran = input("Ingin membeli baju ukuran apa ? ")
    if (ukuran == 'S'):
        jumlah_barang = int(input("Jumlah yang ingin dibeli per kodi : "))
        barang.append('Baju ukuran S')
        jumlah += harga_baju_ukuran_s * jumlah_barang
    elif (ukuran == 'L'):
        jumlah_barang = int(input("Jumlah yang ingin dibeli per kodi : "))
        barang.append('Baju ukuran L')
        jumlah += (harga_baju_ukuran_s * 1.1) * jumlah_barang
    elif (ukuran == 'XL'):
        jumlah_barang = int(input("Jumlah yang ingin dibeli per kodi : "))
        barang.append('Baju ukuran XL')
        jumlah += (harga_baju_ukuran_s * 1.5) * jumlah_barang
    elif (ukuran == 'XXL'):
        jumlah_barang = int(input("Jumlah yang ingin dibeli per kodi : "))
        barang.append('Baju ukuran XXL')
        jumlah += (harga_baju_ukuran_s * 1.7) * jumlah_barang
    else:
        print("Barang tidak ada")

    lanjut = input("Ingin membeli baju ukuran lain ? (y/t) : ")
    if lanjut == 't':
        print()
        break


print(f"Anda akan membeli  {barang}")
print(f"Jumlah {jumlah:,}")

if jumlah >= 10000000:
    print("Anda mendapatkan potongan 10%")
    harga_potongan = jumlah * (10/100)
    total = jumlah - harga_potongan
    print(f"Jadi totalnya adalah {total:,}")

elif jumlah >= 5000000 and jumlah <= 10000000:
    print("Anda mendapatkan potongan 3%")
    harga_potongan = jumlah * (3/100)
    total = jumlah - harga_potongan
    print(f"Total potongan anda Rp {harga_potongan}")
    print(f"Jadi totalnya adalah Rp {total:,}")
