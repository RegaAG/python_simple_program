print("Kalkulator Sederhana")
print("Powered by Rega")

print("="*50)

angka_1 = float(input("Masukan angka pertama  : "))
operator = input("Pilih operator (+,-,x,/)    : ")
angka_2 = float(input("Masukan angka kedua    : "))

print("="*50)

if operator == '+':
    a = angka_1 + angka_2
    print(angka_1, "+", angka_2, "=", a)

elif operator == '-':
    a = angka_1 - angka_2
    print(angka_1, "-", angka_2, "=", a)

elif operator == 'x':
    a = angka_1 * angka_2
    print(angka_1, "x", angka_2, "=", a)

elif operator == '/':
    a = angka_1 / angka_2
    print(angka_1, "/", angka_2, "=", a)

else:
    print("Operator tidak valid")

print("Hallo Cantikku, Apa kabarrr")