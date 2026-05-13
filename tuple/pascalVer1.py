# ── Segitiga Pascal dengan Tuple ─────────────────────────

def segitiga_pascal(n):
    # ① Validasi input
    if n <= 0:
        return "Input tidak valid."

    # ② Mulai dengan baris pertama
    segitiga = [(1,)]

    # ③ Bangun baris berikutnya satu per satu
    for _ in range(1, n):
        prev     = segitiga[-1]        # ambil baris terakhir
        baris    = [1]                  # ujung kiri selalu 1

        for i in range(1, len(prev)):
            baris.append(prev[i-1] + prev[i])  # jumlahkan dua atas

        baris.append(1)               # ujung kanan selalu 1
        segitiga.append(tuple(baris)) # simpan sebagai tuple

    # ④ Kumpulkan semua angka unik di seluruh segitiga
    semua_angka = set(
        x
        for baris in segitiga
        for x in baris
    )
    jumlah_unik = len(semua_angka)

    # ⑤ Gabungkan semua baris + jumlah_unik jadi 1 tuple besar
    return tuple(segitiga) + (jumlah_unik,)


# ── Main ─────────────────────────────────────────────────
n = int(input())
print("Hasil Prof :", segitiga_pascal(n))