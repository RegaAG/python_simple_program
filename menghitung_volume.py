nama = input("Nama : ")
npm = input("NPM : ")
kelas = input("Kelas : ")
jurusan = input("Jurusan : ")
fakultas = input("Fakultas : ")
nama_universitas = input("Nama Universitas : ")
ttl = input("Tempat, tanggal lahir : ")
asal_daerah = input("Asal Daerah : ")
domisili = input("Domisili : ")

print("""
1. Mencarri volume balok
2. Mencarri volume kubus
3. Mencarri volume bola
4. Mencarri volume kerucut
5. Mencarri volume perisma segitiga
6. Mencarri volume perisma tabung
""")

while True:
    opsi = int(input("Pilih program (1-6): "))
    if (opsi == 1):
        p = float(input("Masukan panjangnya : "))
        l = float(input("Masukan lebarnya : "))
        t = float(input("Masukan tingginya : "))
        v = (p * l * t)
        print("volumenya adalah ",v," cm")
    
    elif (opsi == 2):
        s = float(input("Masukan nilai sisi : "))
        v = (s * s * s)
        print("volumenya adalah",v,"cm")

    else:
        print("PROGRAM TIDAK ADA")







    lanjut = input("Ingin mencoba program lain ? (y/t) : ")
    if lanjut == 't':
        print()
        break