try:
    sisi1 = int(input("Masukkan besar sisi pertama: "))
    sisi2 = int(input("Masukkan besar sisi kedua: "))
    sisi3 = int(input("Masukkan besar sisi ketiga: "))

    # if sisi1 == sisi2 == sisi3:
    #     print("Segitiga sama sisi")
    # elif sisi1 == sisi2 or sisi2 == sisi3 or sisi3 == sisi1:
    #     print("Segitiga sama kaki")
    # else:
    #     print("Segitiga sembarang")
    kategori = ("3 sisi sama" if sisi1 == sisi2 == sisi3 else "2 sisi sama" if sisi1 == sisi2 or sisi2 == sisi3 or sisi3 == sisi1 else "Tidak ada yang sama")
    
    print(kategori)

except ValueError:
    print("Format Salah!")