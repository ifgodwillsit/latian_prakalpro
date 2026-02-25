try:
    bilangan = int(input("Masukkan bilangan: "))

    hasilBilangan = ("nol" if bilangan == 0 else "positif" if bilangan >= 0 else "negatif")
    print(hasilBilangan)
except:
    print("Format yang anda masukkan salah")