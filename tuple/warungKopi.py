# ── Warung Kopi Pak Breww ────────────────────────────────

def tentukan_status(total):
    if total >= 50000:
        return "VIP"
    elif total >= 20000:
        return "Reguler"
    else:
        return "Hemat"


def rekap_tagihan(pesanan):
    # ① Cek kosong
    if not pesanan:
        return "Warung sepi hari ini."

    # ② Akumulasi per pelanggan
    #    key   = nama.lower()
    #    value = [nama_title, total_tagihan]
    akum = {}

    for nama, menu, jumlah, harga in pesanan:
        key      = nama.lower()
        subtotal = jumlah * harga
        if key in akum:
            akum[key][1] += subtotal
        else:
            akum[key] = [nama.title(), subtotal]

    # ③ Bangun list hasil
    hasil = []
    for key in akum:
        nama_t, total = akum[key]
        status = tentukan_status(total)
        hasil.append((nama_t, total, status))

    # ④ Sort: total desc → nama asc
    hasil.sort(key=lambda x: (-x[1], x[0]))

    return tuple(hasil)


# ── Main ─────────────────────────────────────────────────
pesanan = eval(input())
print("Hasil Prof :", rekap_tagihan(pesanan))