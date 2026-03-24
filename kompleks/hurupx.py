#buat huruf x dengan karakter *
#aturannya adalah vertikal harus ganjil
#contoh input verti = 7
#*           *
#  *       *
#    *   *
#      *   
#    *   *
#  *       *
#*           *

def hurupx(verti):
    if verti % 2 == 1:
        setengah = verti // 2
        for i in range(verti):
            if i < setengah:
                spasi_kiri = i * 2
                spasi_tengah = (setengah - i - 1) * 4 + 3
                print(" " * spasi_kiri + "*" + " " * spasi_tengah + "*")
            elif i == setengah:
                spasi_kiri = setengah * 2
                print(" " * spasi_kiri + "*")
            else:
                j = verti - i - 1
                spasi_kiri = j * 2
                spasi_tengah = (setengah - j - 1) * 4 + 3
                print(" " * spasi_kiri + "*" + " " * spasi_tengah + "*")
    else:
        print("Gak iso rek!")
    pass

verti = int(input("Tinggix:"))
hurupx(verti)