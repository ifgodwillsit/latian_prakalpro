def rekap_kasir(data):
    # Rule 8: kembalikan string jika data kosong
    if not data:
        return "Tidak ada data transaksi."
 
    # Rule 1: kelompokkan transaksi berdasarkan id_kasir
    kasir = {}
    for id_kasir, nama_kasir, kategori, jumlah_item, harga_satuan in data:
        if id_kasir not in kasir:
            kasir[id_kasir] = {"nama": nama_kasir, "transaksi": []}
        kasir[id_kasir]["transaksi"].append((kategori, jumlah_item, harga_satuan))
 
    hasil = []
    for id_kasir, info in kasir.items():
        nama = info["nama"]
        transaksi = info["transaksi"]
 
        # Rule 2: total pendapatan
        total_pendapatan = round(
            sum(jumlah * harga for _, jumlah, harga in transaksi), 2
        )
 
        # Rule 3: rata-rata transaksi
        rata_rata = round(total_pendapatan / len(transaksi), 2)
 
        # Rule 4: kategori_terlaris berdasarkan total item (pertama jika seri)
        total_item_per_kategori = {}
        for kategori, jumlah, _ in transaksi:
            if kategori not in total_item_per_kategori:
                total_item_per_kategori[kategori] = 0
            total_item_per_kategori[kategori] += jumlah
 
        kategori_terlaris = max(total_item_per_kategori,
                                key=lambda k: total_item_per_kategori[k])
 
        # Rule 5: bonus berdasarkan total pendapatan
        if total_pendapatan >= 5_000_000:
            bonus = 500_000
        elif total_pendapatan >= 3_000_000:
            bonus = 300_000
        elif total_pendapatan >= 1_000_000:
            bonus = 100_000
        else:
            bonus = 0
 
        hasil.append((id_kasir, nama, total_pendapatan, rata_rata,
                       kategori_terlaris, bonus))
 
    # Rule 7: urutkan total_pendapatan descending, id_kasir ascending jika sama
    hasil.sort(key=lambda x: (-x[2], x[0]))
 
    # Rule 6: kembalikan sebagai tuple besar
    return tuple(hasil)

data = eval(input())
print(rekap_kasir(data))