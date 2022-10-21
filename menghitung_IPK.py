print("MENGHITUNG IPK MAHASISWA")

nama = input("Nama : ")
nim = input("NIM : ")
jumlah_matkul = int(input("Jumlah mata kuliah : "))

for i in range(0, jumlah_matkul):
    print()
    nama_matkul = input("Nama mata kuliah : ")
    sks = input("Jumlah SKS : ")
    nilai = float(input("Nilai : "))
    print()
