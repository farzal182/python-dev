# list program untuk mengkonversikan suhu

# Input Data

print("\nKONVERSI UKUR SUHU\n")

celcius = int(input("Suhu dalam celcius : "))
print("suhu adalah ",int(celcius), "°C")

# Konversi ke Fahreinheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah ",int(fahrenheit), "°F")

# Konversi ke Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ",int(reamur), "°R")

# Konversi ke Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ",int(kelvin), "°K")
