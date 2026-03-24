#buat output berupa anak panah dengan karakter bintang, aturannya seperti ini:
#menurun harus ganjil
#buat bilah panahnya dengan aturan dari ujung garis dengan panjang 1/4, pastikan sejajar sisi atas dan bawah
#mendatar boleh ganjil atau genap
#contoh:
#           *
#             *
#               *
#                 *
# * * * * * * * * * *
#                 *
#               *
#             *
#           *
def panah(hori, verti):
    if verti % 2 == 1:
        setengah = int(verti / 2 + 1)
        n = hori - setengah
        while verti > setengah:
            print("  " * n + "*", end="\n")
            n += 1
            setengah += 1
        print("* " * hori)
        setengah = int(verti / 2 + 1)
        n = hori - 2
        while verti > setengah:
            print("  " * n + "*", end="\n")
            n -= 1
            setengah += 1
    else:
        print("Vertikal harus ganjil")


hori = int(input("Panjang horizontal:"))
verti = int(input("Tinggi panah:"))
panah(hori, verti)