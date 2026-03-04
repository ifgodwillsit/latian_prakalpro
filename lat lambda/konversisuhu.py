fahrenheit = lambda a: (9/5) * a + 32
reamur = lambda a : 0.8 * a
a = int(input("Celcius: "))
print(f"Fahrenheit: {str(fahrenheit(a)):.2}")
print(f"Reamur: {str(reamur(a)):.2}")