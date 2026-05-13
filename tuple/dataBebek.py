def kumpulkan_bebek(n):
    # Baca input dan simpan sebagai tuple (nama, berat)
    # Kembalikan tuple of tuples, contoh:
    # (("Koko", 300), ("Lili", 450), ...)
    bebek = []
    for _ in range(n):
        data = input().split()
        ### ISIMU DI SINI ###
        # nama = ???
        # berat = ???
        # bebek.append(???)
        nama = data[0]
        berat = int(data[1])
        bebek.append((nama, berat))
    return tuple(bebek)


def bebek_terberat(data_bebek):
    # TODO: Kembalikan tuple (nama, berat) dari bebek terberat
    ### ISIMU DI SINI ###
    return max(tuple(data_bebek, key = lambda bebek: bebek[1]))
        


def rata_rata_berat(data_bebek):
    # TODO: Hitung rata-rata berat semua bebek
    # Kembalikan float dibulatkan 2 desimal
    ### ISIMU DI SINI ###
    total = sum(bebek[1] for bebek in data_bebek)
    return round(total / len(data_bebek), 2)


def hitung_di_atas_rata(data_bebek, rata):
    # TODO: Hitung berapa bebek yang beratnya > rata
    ### ISIMU DI SINI ###
    return sum(1 for bebek in data_bebek if bebek[1] > rata)


# === PROGRAM UTAMA ===
n = int(input())
data = kumpulkan_bebek(n)

terberat = bebek_terberat(data)
rata = rata_rata_berat(data)
di_atas = hitung_di_atas_rata(data, rata)

print(f"Bebek terberat: {terberat[0]} ({terberat[1]} gram)")
print(f"Rata-rata berat: {rata} gram")
print(f"Bebek di atas rata-rata: {di_atas} ekor")