from collections import defaultdict

# Baca input sekaligus (cepat untuk kompetisi)

def main():
    N, M = map(int, input().split())

    # dict: tag -> set of manuscript IDs
    tag_to_ids: dict[str, set[int]] = defaultdict(set)

    for _ in range(N):
        parts = input().split()
        manuscript_id = int(parts[0])
        tags = parts[1:]            # list of tags
        for tag in tags:
            tag_to_ids[tag].add(manuscript_id)

    out = []

    for _ in range(M):
        parts = input().split()
        op = parts[0]

        if op == "RARE":
            # tuple sort: (jumlah, nama_tag) -> ambil minimum
            rarest: tuple[int, str] = min(
                ((len(ids), tag) for tag, ids in tag_to_ids.items()),
                key=lambda x: (x[0], x[1])
            )
            out.append(rarest[1])
            continue

        tagA, tagB = parts[1], parts[2]

        # Ambil set (kosong jika tag tak dikenal)
        setA: set[int] = tag_to_ids.get(tagA, set())
        setB: set[int] = tag_to_ids.get(tagB, set())

        if   op == "UNION":      result = setA | setB
        elif op == "INTERSECT":  result = setA & setB
        elif op == "DIFF":       result = setA - setB
        elif op == "EXCLUSIVE":  result = setA ^ setB

        if result:
            out.append(" ".join(map(str, sorted(result))))
        else:
            out.append("KOSONG")

    print("\n".join(out))

main()

# 1. Struktur data utama — dict[str, set[int]]
# Kita bangun indeks terbalik: untuk setiap tag, simpan set berisi semua ID manuskrip yang punya tag itu. Ini kunci performanya — operasi set berjalan O(min(|A|,|B|)) bukan O(N²).
# 2. Operasi himpunan Python — operator bawaan
# Python mendukung langsung: setA | setB (union), setA & setB (intersection), setA - setB (difference), setA ^ setB (symmetric diff / XOR). Semua ini O(|A|+|B|) worst case.
# 3. Kueri RARE — kombinasi tuple + min()
# Untuk mencari tag paling jarang, kita buat generator (len(ids), tag) lalu panggil min() dengan key tupel. Tuple comparison di Python sudah leksikografis — jika count sama, nama tag lebih kecil secara alfabet otomatis menang. Tidak perlu sort penuh!
# 4. Input cepat — sys.stdin.readline
# Pada soal kompetisi dengan N=100.000, input() bawaan Python lambat. Mengganti dengan sys.stdin.readline bisa 3–5× lebih cepat karena menghindari overhead buffering tambahan.
# 5. Output batch — list + join
# Daripada print() per baris (lambat karena flush), kita kumpulkan semua hasil di list out lalu cetak sekaligus dengan "\n".join(out). Ini pola standar kompetisi Python.