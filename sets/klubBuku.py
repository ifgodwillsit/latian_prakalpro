from collections import defaultdict

# koleksi: anggota -> set buku (defaultdict agar anggota baru otomatis set kosong)
koleksi: dict[str, set[str]] = defaultdict(set)

N = int(input())
for _ in range(N):
    parts = input().split()
    nama  = parts[0]
    K     = int(parts[1])
    buku  = set(parts[2:2+K])
    koleksi[nama] = buku

def fmt(s: set) -> str:
    return " ".join(sorted(s)) if s else "KOSONG"

Q   = int(input())
out = []

for _ in range(Q):
    parts = input().split()
    op    = parts[0]

    if op == "TAMBAH":
        koleksi[parts[1]].add(parts[2])    # set.add() otomatis abaikan duplikat

    elif op == "HAPUS":
        koleksi[parts[1]].discard(parts[2]) # discard() aman meski elemen tidak ada

    elif op == "KOLEKSI":
        out.append(fmt(koleksi[parts[1]]))

    elif op == "SAMA":
        out.append(fmt(koleksi[parts[1]] & koleksi[parts[2]]))

    elif op == "TERBANYAK":
        maks = max(len(v) for v in koleksi.values())
        seri = sorted(k for k, v in koleksi.items() if len(v) == maks)
        out.append(" ".join(seri))

    elif op == "REKOMENDASI":
        # buku milik B yang belum dimiliki A = B - A
        out.append(fmt(koleksi[parts[2]] - koleksi[parts[1]]))

print("\n".join(out))