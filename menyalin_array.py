nilaiMHS = []
nilaiMHS_UPG = []

jumlah = int(input("Jumlah nilai yang ingin dimasukan : "))

for i in range(0, jumlah):
    nilai = int(input("Masukan nilai : "))
    nilaiMHS.append(nilai)

nilaiMHS_UPG = nilaiMHS

print("Nilai MHS : ", nilaiMHS)
print("Nilai MHS UPG : ", nilaiMHS_UPG)

