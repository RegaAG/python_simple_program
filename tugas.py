L1 = []
L2 = []
L3 = []

angka1_L1 = int(input("Masukan angka pertama di L1 = "))
angka2_L1 = int(input("Masukan angka kedua di L1 = "))
angka3_L1 = int(input("Masukan angka ketiga di L1 = "))
angka4_L1 = int(input("Masukan angka keempat di L1 = "))
print("=" * 25)

angka1_L2 = int(input("Masukan angka pertama di L2 = "))
angka2_L2 = int(input("Masukan angka kedua di L2 = "))
angka3_L2 = int(input("Masukan angka ketiga di L2 = "))
angka4_L2 = int(input("Masukan angka keempat di L2 = "))
print("=" * 25)

angka1_L3 = int(input("Masukan angka pertama di L3 = "))
angka2_L3 = int(input("Masukan angka kedua di L3 = "))
angka3_L3 = int(input("Masukan angka ketiga di L3 = "))
angka4_L3 = int(input("Masukan angka keempat di L3 = "))
print("=" * 25)

L1.append(angka1_L1)
L1.append(angka2_L1)
L1.append(angka3_L1)
L1.append(angka4_L1)

L2.append(angka1_L2)
L2.append(angka2_L2)
L2.append(angka3_L2)
L2.append(angka4_L2)

L3.append(angka1_L3)
L3.append(angka2_L3)
L3.append(angka3_L3)
L3.append(angka4_L3)

jumlah_1 = angka1_L1 + angka1_L2 + angka1_L3
jumlah_2 = angka2_L1 + angka2_L2 + angka2_L3
jumlah_3 = angka3_L1 + angka3_L2 + angka3_L3

print("L1", L1)
print("L2", L2)
print("L3", L3)
print("List 3 plus", jumlah_1, jumlah_2, jumlah_3)
