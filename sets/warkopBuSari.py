N = int(input())

# Simpan set pelanggan per hari (index 0 = hari ke-1)
hari: list[set[str]] = []

# Hitung berapa hari tiap pelanggan datang
frekuensi: dict[str, int] = {}

for _ in range(N):
    parts  = input().split()
    tamu   = set(parts[1:])         # abaikan angka K di depan
    hari.append(tamu)
    for nama in tamu:
        frekuensi[nama] = frekuensi.get(nama, 0) + 1

# Semua pelanggan yang pernah datang
semua: set[str] = set(frekuensi.keys())

Q = int(input())
out = []

for _ in range(Q):
    parts = input().split()
    op    = parts[0]

    if op == "SETIA":
        # pelanggan yang frekuensinya == N (hadir setiap hari)
        hasil = {nama for nama, freq in frekuensi.items() if freq == N}
        out.append(" ".join(sorted(hasil)) if hasil else "KOSONG")

    elif op == "SEKALI":
        # pelanggan yang frekuensinya == 1
        hasil = {nama for nama, freq in frekuensi.items() if freq == 1}
        out.append(" ".join(sorted(hasil)) if hasil else "KOSONG")

    elif op == "HARI_TERLARIS":
        # cari jumlah tamu maksimum
        maks = max(len(h) for h in hari)
        # kumpulkan semua hari yang mencapai maksimum (1-indexed)
        terlaris = [
            str(i + 1) for i, h in enumerate(hari)
            if len(h) == maks
        ]
        out.append(" ".join(terlaris))

    elif op == "CEK":
        nama = parts[1]
        out.append(str(frekuensi.get(nama, 0)))

    elif op == "BARU":
        h = int(parts[1]) - 1       # konversi ke index 0-based
        # union semua hari SEBELUM hari h
        pernah_datang: set[str] = set()
        for i in range(h):
            pernah_datang |= hari[i]
        # pelanggan hari h yang belum pernah muncul sebelumnya
        baru = hari[h] - pernah_datang
        out.append(" ".join(sorted(baru)) if baru else "KOSONG")

print("\n".join(out))