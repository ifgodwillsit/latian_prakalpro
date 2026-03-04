try:
    usia = int(input("Masukkan usia anda: "))
    print("Balita" if 0 < usia < 6 else "Kanak-kanak" if 5 < usia < 12 else "Remaja" if 11 < usia < 26 else "Dewasa" if 25 < usia < 46 else "Lansia")
except ValueError:
    print("Input bilangan bulat!")
    