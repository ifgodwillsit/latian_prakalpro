# Baca daftar tamu langsung ke set
A = int(input())
raka: set[str] = set(input().split())

B = int(input())
dina: set[str] = set(input().split())

Q = int(input())
out = []

for _ in range(Q):
    parts = input().split()
    op    = parts[0]

    if op == "KEDUANYA":
        hasil = raka & dina          # intersection

    elif op == "SEMUA":
        hasil = raka | dina          # union

    elif op == "HANYA_RAKA":
        hasil = raka - dina          # difference

    elif op == "HANYA_DINA":
        hasil = dina - raka

    if op in ("KEDUANYA", "SEMUA", "HANYA_RAKA", "HANYA_DINA"):
        if hasil:
            out.append(" ".join(sorted(hasil)))
        else:
            out.append("KOSONG")

    elif op == "TOTAL":
        out.append(str(len(raka | dina)))

    elif op == "CEK":
        nama = parts[1]
        # diundang keduanya = ada di intersection
        if nama in raka & dina:
            out.append("YA")
        else:
            out.append("TIDAK")

print("\n".join(out))