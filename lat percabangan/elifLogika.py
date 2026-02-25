try:
    bulan = int(input("Masukkan bulan (1-12): "))
    a = 31
    b = 30
    c = 28

    # if bulan == 1 or bulan == 3 or bulan == 7 or bulan == 9 or bulan == 11:
    #     print(f"Jumlah hari: {a}")
    # elif bulan == 2:
    #     print(f"Jumlah hari: {c}")
    # elif bulan == 4 or bulan == 6 or bulan == 8 or bulan == 10 or bulan == 12:
    #     print(f"Jumlah hari: {b}")
    # elif bulan < 1 or bulan > 12:
    #     print("Range angka hanya 1-12!")
    print(f"Jumlah hari: {a}" if bulan == 1 or bulan == 3 or bulan == 7 or bulan == 9 or bulan == 11 else
          f"Jumlah hari: {c}" if bulan == 2 else
          f"Jumlah hari: {b}" if bulan == 4 or bulan == 6 or bulan == 8 or bulan == 10 or bulan == 12 else
          "Range angka hanya 1-12!")
except ValueError:
    print("Input harus berupa angka!")