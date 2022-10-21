nilai = int(input("Masukan nilai : "))
count = 0
summ = 0

for i in range(1, nilai):
    if i % 2 == 0:
        print(i, end=' ')
        count = count + 1
        summ = summ + 1


print()
print(f"Bilangan diatas ada {count}")
