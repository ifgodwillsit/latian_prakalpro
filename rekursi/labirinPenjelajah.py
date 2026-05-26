N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

# Arah diurutkan: Bawah, Kanan, Kiri, Atas (untuk leksikografis)
ARAH = [(1,0), (0,1), (0,-1), (-1,0)]

jumlah_jalur  = 0
jalur_terpendek = None

def backtrack(r: int, c: int,
              path: list,
              visited: set) -> None:
    global jumlah_jalur, jalur_terpendek

    # Base case: sampai tujuan
    if r == N-1 and c == M-1:
        jumlah_jalur += 1
        # Update jalur terpendek (lebih pendek, atau sama panjang tapi lebih kecil leksikografis)
        if (jalur_terpendek is None
                or len(path) < len(jalur_terpendek)
                or (len(path) == len(jalur_terpendek)
                    and path < jalur_terpendek)):
            jalur_terpendek = path.copy()
        return

    # Recursive case: coba semua arah
    for dr, dc in ARAH:
        nr, nc = r + dr, c + dc
        # Cek batas, bukan tembok, belum dikunjungi
        if (0 <= nr < N and 0 <= nc < M
                and grid[nr][nc] == 0
                and (nr, nc) not in visited):
            # Tandai dikunjungi
            visited.add((nr, nc))
            path.append((nr, nc))

            backtrack(nr, nc, path, visited)  # rekursi

            # Backtrack: batalkan pilihan
            visited.discard((nr, nc))
            path.pop()

# Mulai dari (0,0)
start_visited = {(0, 0)}
start_path    = [(0, 0)]
backtrack(0, 0, start_path, start_visited)

# Output
if jumlah_jalur > 0:
    print("ADA")
    print(jumlah_jalur)
    print(" ".join(f"({r},{c})" for r, c in jalur_terpendek))
else:
    print("TIDAK ADA")
    print(0)
    print("TIDAK ADA")