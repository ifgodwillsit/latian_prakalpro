def perkalian (a, b):
    i = 1
    for i in range(b):
        if i == b - 1:
            print(str(a) + " = ", end = "")
        else:
            print(str(a) + " + ", end = "")
    print(str(a * b))

run = True
while (run):
    print("Perkalian")
    try:
        a = int(input("Angka Pertama: "))
        b = int(input("Angka Kedua: "))
        print("===============")
        c = perkalian(a, b)
        keterangan = input("Lanjut tidak? (Lanjut ketik T): ")
        if keterangan == "T":
            print("Restart Program")
        else:
            break
    except: 
        print("===============")
        print("Jenis Format Salah")
        