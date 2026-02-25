fahrenheit = lambda a: (9/5) * a + 32
reamur = lambda a : 0.8 * a
celcius = int(input("Celcius: "))
print(f"Fahrenheit: {str(fahrenheit(celcius)):.2}")
print(f"Reamur: {str(reamur(celcius)):.2}")