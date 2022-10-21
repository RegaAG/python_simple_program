# input user
print("*"*25)
print("ISI DATA TANGGAL PERTAMA")
print("*"*25)
tanggal_pertama = int(input("Tanggal : "))
bulan_pertama = int(input("Bulan  : "))
tahun_pertama = int(input("Tahun : "))
print(
    f"Tanggal pertama adalah {tanggal_pertama} - {bulan_pertama} - {tahun_pertama}")
print("-"*25)
print("*"*25)
print("ISI DATA TANGGAL KEDUA")
print("*"*25)
tanggal_kedua = int(input("Tanggal : "))
bulan_kedua = int(input("Bulan  : "))
tahun_kedua = int(input("Tahun : "))
print(
    f"Tanggal kedua adalah {tanggal_kedua} - {bulan_kedua} - {tahun_kedua}")

# proses
selisih_hari = (tanggal_kedua + (30 * bulan_kedua) + (365 * tahun_kedua)) - \
    (tanggal_pertama + (30 * bulan_pertama) + (365 * tahun_pertama))

# output
print("-"*25)
print(
    f"SELISIH HARI DARI {tanggal_pertama} - {bulan_pertama} - {tahun_pertama} <-----> {tanggal_kedua} - {bulan_kedua} - {tahun_kedua} ADALAH : {selisih_hari} HARI")
