def rekap_nilai(data):
    # Rule 7: kembalikan string jika data kosong
    if not data:
        return "Tidak ada data nilai."
 
    # Rule 1: kelompokkan nilai berdasarkan NIM
    mahasiswa = {}
    for nim, nama, mata_kuliah, nilai in data:
        if nim not in mahasiswa:
            mahasiswa[nim] = {"nama": nama, "matkul": []}
        mahasiswa[nim]["matkul"].append((mata_kuliah, nilai))
 
    hasil = []
    for nim, info in mahasiswa.items():
        nama = info["nama"]
        matkul_list = info["matkul"]
 
        # Rule 2: hitung IPK (rata-rata nilai, 2 desimal)
        ipk = round(sum(n for _, n in matkul_list) / len(matkul_list), 2)
 
        # Rule 3: tentukan predikat
        if ipk >= 85:
            predikat = "Cumlaude"
        elif ipk >= 70:
            predikat = "Memuaskan"
        elif ipk >= 55:
            predikat = "Cukup"
        else:
            predikat = "Perlu Bimbingan"
 
        # Rule 4: mata kuliah dengan nilai tertinggi (pertama jika seri)
        mata_kuliah_terbaik = max(matkul_list, key=lambda x: x[1])[0]
 
        hasil.append((nim, nama, ipk, predikat, mata_kuliah_terbaik))
 
    # Rule 6: urutkan IPK descending, NIM ascending jika IPK sama
    hasil.sort(key=lambda x: (-x[2], x[0]))
 
    # Rule 5: kembalikan sebagai tuple besar
    return tuple(hasil)

data = eval(input())
print(rekap_nilai(data))