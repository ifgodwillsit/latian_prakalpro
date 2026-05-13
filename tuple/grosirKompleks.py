# ── Smart Inventory Tracker ──────────────────────────────

def hitung_diskon(jumlah):
    if jumlah >= 10:
        return 0.15
    elif jumlah >= 5:
        return 0.10
    else:
        return 0.0


def buat_laporan(transaksi):
    # Kasus kosong
    if not transaksi:
        return "Tidak ada transaksi hari ini."

    # Akumulator: key = nama.lower()
    # value = [nama_canonical, jumlah, harga_satuan, kategori]
    akum = {}

    for nama, jumlah, harga, kategori in transaksi:
        key = nama.lower()
        if key in akum:
            akum[key][1] += jumlah          # tambah kuantitas
            akum[key][2]  = harga           # update harga terakhir
            akum[key][3]  = kategori        # update kategori terakhir
        else:
            akum[key] = [nama.title(), jumlah, harga, kategori]

    # Hitung total bayar setelah diskon
    hasil = []
    for key in akum:
        nama_c, qty, harga, kat = akum[key]
        diskon   = hitung_diskon(qty)
        subtotal = qty * harga
        total    = int(subtotal * (1 - diskon))
        hasil.append((nama_c, kat, total))

    # Sort: kategori A→Z, lalu total_bayar Z→A (terbesar duluan)
    hasil.sort(key=lambda x: (x[1], -x[2]))

    return tuple(hasil)


# ── Main ─────────────────────────────────────────────────
transaksi = eval(input())
print("Hasil Prof :", buat_laporan(transaksi))