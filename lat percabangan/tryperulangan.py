inputs = (input("Masukkan usia anda"))
try:
    usia = int(inputs)
    if usia <= 5:
        print("Balita")
    elif usia <= 11:
        print("Anak-anak")
    elif usia <= 25:
        print("Remaja")
    elif usia <= 45:
        print("Dewasa")
    else:
        print("Lansia")
except:
    print("Salah input!")