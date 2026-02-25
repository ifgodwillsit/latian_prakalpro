angka = int(input("Masukkan bilangan yang ingin difaktorialkan: "))
i = 1
hasil = 1
while i <= angka:
    hasil = hasil * i
    i = i + 1
    
print(hasil)