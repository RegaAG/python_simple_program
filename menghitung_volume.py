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
1. PROGRAM MENGHITUNG VOLUME BALOK
2. PROGRAM MENGHITUNG VOLUME KUBUS
3. PROGRAM MENGHITUNG VOLUME BOLA
4. PROGRAM MENGHITUNG VOLUME KERUCUT
5. PROGRAM MENGHITUNG VOLUME PRISMA SEGITIGA
6. PROGRAM MENGHITUNG VOLUME PRISMA TABUNG
""")

while True:
    opsi = int(input("Pilih program (1-6): "))
    if (opsi == 1):
        print("""

        PROGRAM MENGHITUNG VOLUME BALOK
        
        """)
        p = int(input("Masukan panjangnya : "))
        l = int(input("Masukan lebarnya : "))
        t = int(input("Masukan tingginya : "))
        v = (p * l * t)
        print(f"VOLUMENYA ADALAH {v:,}")
    
    elif (opsi == 2):
        print("""

        PROGRAM MENGHITUNG VOLUME KUBUS
        
        """)
        s = int(input("Masukan nilai sisi : "))
        v = (s * s * s)
        print(f"VOLUMENYA ADALAH {v:,}")

    elif (opsi == 3):
        print("""

        PROGRAM MENGHITUNG VOLUME BOLA
        
        """)
        r = int(input("Masukan nilai r : "))
        v = (4/3 * 3.14 * r * r * r)
        print(f"VOLUMENYA ADALAH {v:,}")

    elif (opsi == 4):
        print("""

        PROGRAM MENGHITUNG VOLUME KERUCUT
        
        """)
        r = int(input("Masukan nilai r : "))
        t = int(input("Masukan nilai t : "))
        v = (1/3 * 3.14 * r * r * t)
        print(f"VOLUMENYA ADALAH {v:,}")


    else:
        print("PROGRAM TIDAK ADA")

    lanjut = input("Ingin mencoba program lain ? (y/t) : ")
    if lanjut == 'y' or lanjut == "Y":
        print()
    else:
        print("PROGRAM SELESAI")
        break