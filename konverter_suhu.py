print("TEMPERATURE CONVERTER")

print("="*50)
print("""
Note : 
1. Celsius to Reamur
2. Celsius to Kelvin
3. Celsius to Fahrenheit
4. Reamur to Celsius
5. Reamur to Kelvin
6. Reamur to Fahrenheit
7. Fahrenheit to Celsius
8. Fahrenheit to Reamur
9. Fahrenheit to Kelvin
10. Kelvin to Celsius
11. Kelvin to Reamur
12. Kelvin to Fahrenheit
""")
print("="*50)

user = int(input("Select operation above (1-12): "))

if user == 1:
    celcius = float(input("Enter the Celsius value: "))
    reamur = (4/5) * celcius
    print(celcius, "celcius =", reamur, "reamur")

elif user == 2:
    celcius = float(input("Enter the Celsius value: "))
    kelvin = celcius + 273
    print(celcius, "celcius =", kelvin, "kelvin")

elif user == 3:
    celcius = float(input("Enter the Celsius value: "))
    fahrenheit = ((9/5) * celcius) + 32
    print(celcius, "celcius =", fahrenheit, "fahrenheit")

elif user == 4:
    reamur = float(input("Enter the remuneration value: "))
    celcius = (5/4) * reamur
    print(reamur, "reamur =", celcius, "celcius")

elif user == 5:
    reamur = float(input("Enter the remuneration value: "))
    kelvin = ((5/4) * reamur) + 273
    print(reamur, "reamur =", kelvin, "kelvin")

elif user == 6:
    reamur = float(input("Enter the remuneration value: "))
    fahrenheit = ((9/4) * reamur) + 32
    print(reamur, "reamur =", fahrenheit, "fahrenheit")

elif user == 7:
    fahrenheit = float(input("Enter Fahrenheit value: "))
    celcius = (5/9) * (fahrenheit - 32)
    print(fahrenheit, "fahrenheit =", celcius, "celcius")

elif user == 8:
    fahrenheit = float(input("Enter Fahrenheit value: "))
    reamur = (4/9) * (fahrenheit - 32)
    print(fahrenheit, "fahrenheit =", reamur, "reamur")

elif user == 9:
    fahrenheit = float(input("Enter Fahrenheit value: "))
    kelvin = (5/9) * (fahrenheit - 32) + 273
    print(fahrenheit, "fahrenheit =", kelvin, "reamur")

elif user == 10:
    kelvin = float(input("Enter the kelvin value: "))
    celcius = kelvin - 273
    print(kelvin, "kelvin =", celcius, "celcius")

elif user == 11:
    kelvin = float(input("Enter the kelvin value: "))
    reamur = (4/5) * (kelvin - 273)
    print(kelvin, "kelvin =", reamur, "reamur")

elif user == 12:
    kelvin = float(input("Enter the kelvin value: "))
    fahrenheit = (9/5) * (kelvin - 273) + 32
    print(kelvin, "kelvin =", fahrenheit, "fahrenheit")

else:
    print("Invalid program")
