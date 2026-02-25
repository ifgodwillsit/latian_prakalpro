try:
    suhu = int(input("Masukkan suhu tubuh: "))
    keterangan = ("Anda demam" if suhu > 37 else
                  "Anda tidak demam"
                  )
    print(keterangan)

except ValueError:
    print("Input berbentuk angka!")