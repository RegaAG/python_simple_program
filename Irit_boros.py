
uang_saku = int(input("Jumlah uang saku perminggu : "))
pengeluaran = int(input("Pengeluaran anda perminggu : "))
print("\n")

hasil = uang_saku - pengeluaran

if hasil > pengeluaran:
    print(
        f"Sisa uang saku anda perminggu adalah {hasil:,} artinya anda adalah orang yang irit")

else:
    print(
        f"Sisa uang saku anda perminggu adalah {hasil:,} artinya anda adalah orang yang boros")