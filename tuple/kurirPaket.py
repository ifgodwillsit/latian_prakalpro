def rekap_kurir(data):
    # Rule 8: kembalikan string jika data kosong
    if not data:
        return "Tidak ada data pengiriman."
 
    # Rule 1: kelompokkan pengiriman berdasarkan id_kurir
    kurir = {}
    for id_kurir, nama_kurir, kota_tujuan, berat_kg, status in data:
        if id_kurir not in kurir:
            kurir[id_kurir] = {"nama": nama_kurir, "pengiriman": []}
        kurir[id_kurir]["pengiriman"].append((kota_tujuan, berat_kg, status))
 
    hasil = []
    for id_kurir, info in kurir.items():
        nama = info["nama"]
        pengiriman = info["pengiriman"]
 
        # Rule 2: total berat paket yang berstatus "terkirim"
        total_berat_terkirim = round(
            sum(berat for _, berat, status in pengiriman if status == "terkirim"),
            2
        )
 
        # Rule 3: tingkat keberhasilan (%)
        jumlah_terkirim = sum(1 for _, _, status in pengiriman if status == "terkirim")
        tingkat_keberhasilan = round(jumlah_terkirim / len(pengiriman) * 100, 2)
 
        # Rule 4: level kurir
        if tingkat_keberhasilan >= 90:
            level = "Platinum"
        elif tingkat_keberhasilan >= 70:
            level = "Gold"
        elif tingkat_keberhasilan >= 50:
            level = "Silver"
        else:
            level = "Bronze"
 
        # Rule 5: kota_favorit — paling sering muncul, pertama jika seri
        frekuensi_kota = {}
        for kota, _, _ in pengiriman:
            if kota not in frekuensi_kota:
                frekuensi_kota[kota] = 0
            frekuensi_kota[kota] += 1
 
        kota_favorit = max(frekuensi_kota, key=lambda k: frekuensi_kota[k])
 
        hasil.append((id_kurir, nama, total_berat_terkirim, tingkat_keberhasilan, level, kota_favorit))
 
    # Rule 7: urutkan tingkat_keberhasilan descending, id_kurir ascending jika sama
    hasil.sort(key=lambda x: (-x[3], x[0]))
 
    # Rule 6: kembalikan sebagai tuple besar
    return tuple(hasil)

data = eval(input())
print(rekap_kurir(data))