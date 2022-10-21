print("SELAMAT DATANG DI TOKO HP")
print("="*30)

print("""
Di jual :
1. Xiaomi Poco X3 NFC, Rp 3.000.000
2. Iphone 12 Pro, Rp 22.000.000
3. Realme C17, Rp 2.800.000
4. Oppo Reno 4 F, 4.300.000
5. Xiaomi Redmi 9 C, Rp 1.000.000
""")

Xiaomi_Poco_X3_NFC = 3000000
Iphone_12_Pro = 22000000
Realme_C17 = 2800000
Oppo_Reno_4_F = 4300000
Xiaomi_Redmi_9_C = 1000000
Samsung_Galaxy_M51 = 5000000
Asus_ROG_Phone_3 = 9000000

print("="*30)

pembeli = int(input("Pengen beli yang mana ? "))


if pembeli == 1:
    jumlah = int(input("Jumlah : "))
    if jumlah < 3:
        print("Anda akan membeli hp Xiaomi Poco X3 NFC sejumlah", jumlah)
        total = Xiaomi_Poco_X3_NFC * jumlah
        print(f"Totalnya = {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya = {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah < 11:
        print("Anda akan membeli hp Xiaomi Poco X3 NFC sejumlah", jumlah)
        total = Xiaomi_Poco_X3_NFC * jumlah - 300000
        print(
            f"Anda mendapatkan potongan harga sebesar Rp 300.000, jadi total pembayarannya hanya {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya = {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah > 10:
        print("Maaf stoknya cuma ada 10")

elif pembeli == 2:
    jumlah = int(input("Jumlah : "))
    if jumlah < 3:
        print("Anda akan membeli hp Iphone 12 Pro sejumlah", jumlah)
        total = Iphone_12_Pro * jumlah
        print(f"Totalnya : {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah < 11:
        print("Anda akan membeli hp Iphone 12 Pro sejumlah", jumlah)
        total = Iphone_12_Pro * jumlah - 300000
        print(
            f"Anda mendapatkan potongan harga sebesar Rp 300.000, jadi total pembayarannya hanya {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah > 10:
        print("Maaf stoknya cuma ada 10")

elif pembeli == 3:
    jumlah = int(input("Jumlah : "))
    if jumlah < 3:
        print("Anda akan membeli hp Realme C17 sejumlah", jumlah)
        total = Realme_C17 * jumlah
        print(f"Totalnya : {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah < 11:
        print("Anda akan membeli hp Realme C17 sejumlah", jumlah)
        total = Realme_C17 * jumlah - 300000
        print(
            f"Anda mendapatkan potongan harga sebesar Rp 300.000, jadi total pembayarannya hanya {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah > 10:
        print("Maaf stoknya cuma ada 10")

elif pembeli == 4:
    jumlah = int(input("Jumlah : "))
    if jumlah < 3:
        print("Anda akan membeli hp Oppo Reno 4 sejumlah", jumlah)
        total = Oppo_Reno_4_F * jumlah
        print(f"Totalnya : {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah < 11:
        print("Anda akan membeli hp Oppo Reno 4 sejumlah", jumlah)
        total = Oppo_Reno_4_F * jumlah - 300000
        print(
            f"Anda mendapatkan potongan harga sebesar Rp 300.000, jadi total pembayarannya hanya {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah > 10:
        print("Maaf stoknya cuma ada 10")

elif pembeli == 5:
    jumlah = int(input("Jumlah : "))
    if jumlah < 3:
        print("Anda akan membeli hp Xiaomi Redmi 9 C sejumlah", jumlah)
        total = Xiaomi_Redmi_9_C * jumlah
        print(f"Totalnya : {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah < 11:
        print("Anda akan membeli hp Xiaomi Redmi 9 C sejumlah", jumlah)
        total = Xiaomi_Redmi_9_C * jumlah - 300000
        print(
            f"Anda mendapatkan potongan harga sebesar Rp 300.000, jadi total pembayarannya hanya {total:,}")
        uang = int(input("Masukan uang anda : "))
        if uang > total:
            kembalian = uang - total
            print(f"Kembaliannya {kembalian:,}")
            print("Terima kasih telah berbelanja di toko kami")
        elif uang < total:
            print("Maaf uang anda tidak cukup")

    elif jumlah > 10:
        print("Maaf stoknya cuma ada 10")
