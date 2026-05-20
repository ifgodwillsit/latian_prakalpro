# ── INPUT: langsung pakai eval(input()) ──────────────────
# Baris 1: dict[str, set[str]]  — peta desa → himpunan gejala
# Baris 2: list[tuple]          — daftar kueri

peta: dict[str, set[str]] = eval(input())
kueri: list[tuple]        = eval(input())

# ── HELPER ───────────────────────────────────────────────
def fmt_set(s: set) -> str:
    """Format set → '{a, b, c}' terurut alfabet, atau '{}'."""
    if not s:
        return "{}"
    return "{" + ", ".join(sorted(s)) + "}"

def get(desa: str) -> set[str]:
    """Ambil set gejala desa; kosong jika tidak dikenal."""
    return peta.get(desa, set())

# ── PROSES KUERI ─────────────────────────────────────────
out = []

for q in kueri:
    op = q[0]  # elemen pertama tuple = nama operasi

    if op == "SAMA":
        _, dA, dB = q               # unpack tuple 3 elemen
        out.append(fmt_set(get(dA) & get(dB)))

    elif op == "GABUNG":
        _, dA, dB = q
        out.append(fmt_set(get(dA) | get(dB)))

    elif op == "UNIK":
        _, dA, dB = q
        out.append(fmt_set(get(dA) - get(dB)))

    elif op == "BEDA":
        _, dA, dB = q
        out.append(fmt_set(get(dA) ^ get(dB)))

    elif op == "BAHAYA":
        _, k = q                    # unpack tuple 2 elemen
        # filter desa dgn gejala > k, lalu sort alfabet
        hasil = sorted(
            d for d, gejala in peta.items()
            if len(gejala) > k
        )
        out.append(", ".join(hasil) if hasil else "-")

    elif op == "SUBWABAH":
        _, dA, dB = q
        # set.issubset() → True jika semua elemen A ada di B
        out.append(str(get(dA).issubset(get(dB))))

print("\n".join(out))



'''1. Mengapa eval(input()) cocok di sini
Input baris pertama adalah dict Python literal — kurung kurawal, kunci string, nilai set. eval() langsung mengurai ini menjadi objek Python asli tanpa parsing manual. Hal yang sama berlaku untuk baris kedua yang berupa list of tuple.
2. Unpack tuple kueri dengan destrukturisasi
_, dA, dB = q memanfaatkan unpacking tuple Python. Karakter _ adalah konvensi untuk "variabel yang tidak dipakai" (nama operasi sudah dicek sebelumnya). Ini lebih bersih daripada q[1], q[2].
3. Operasi set bawaan Python
Karena eval() menghasilkan objek set asli (bukan list atau string), kita bisa langsung pakai operator: & intersect, | union, - difference, ^ symmetric diff, dan method .issubset() — semua O(n).
4. Kueri BAHAYA — filter + sort
Gunakan generator expression di dalam sorted() untuk filter desa sekaligus mengurutkan. Lebih efisien dibanding membuat list terlebih dahulu karena sorted() menerima iterable langsung.
5. fmt_set — format output konsisten
Helper fmt_set() menjamin output selalu terurut alfabet dan berbentuk {a, b, c}. Penting karena set Python tidak punya urutan — mencetak str(set) langsung akan menghasilkan urutan acak yang tidak deterministik.

Inilah kenapa soal ini dirancang ulang supaya eval(input()) masuk akal secara teknis:

Baris 1 diketik sebagai dict literal → eval() langsung jadi dict[str, set[str]] tanpa parsing manual
Baris 2 diketik sebagai list of tuple literal → eval() langsung jadi struktur kueri siap pakai
Karena hasilnya sudah objek set Python asli, semua operator &, |, -, ^, dan .issubset() langsung bisa dipakai tanpa konversi apapun. Ini adalah kasus di mana eval(input()) benar-benar menghemat kode secara signifikan dibanding parsing manual.'''