digit_kanan = lambda a, b, c: True if a % 10 == b % 10 or b % 10 == c %10 or c % 10 == a % 10 else False

a = int(input("Nilai pertama: "))
b = int(input("Nilai kedua: "))
c = int(input("Nilai ketiga: "))

print(digit_kanan(a, b, c))