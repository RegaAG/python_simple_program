print("Menghitung gaji bersih karywan")
print("\n")

# input karyawan
nama = str(input("Nama Karyawan : "))
alamat = str(input("Alamat : "))
gaji_pokok = int(input("Gaji Pokok : "))
print("\n")

# penghitungn gaji bersih
tunjangan = 0.15 * gaji_pokok
pajak = 0.075 * gaji_pokok
gaji_bersih = gaji_pokok + tunjangan - pajak

# output
print(f"Nama : {nama}")
print(f"Gaji Pokok Anda Adalah : {gaji_pokok:,}")
print(f"Tunjangan Anda Sebesar : {tunjangan:,}")
print(f"Pajak Penghasilan Anda Sebesar : {pajak:,}")
print(f"Maka Gaji Bersih Anda Adalah : {gaji_bersih:,}")
print("\n")