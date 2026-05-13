# ── Flight Route Analyzer ────────────────────────────────

def parse_menit(jam_str):
    h, m = jam_str.split(":")
    return int(h) * 60 + int(m)


def hitung_durasi(bgt, tiba):
    selisih = parse_menit(tiba) - parse_menit(bgt)
    if selisih < 0:
        selisih += 1440          # lewat tengah malam
    return selisih


def tentukan_status(avg_lf):
    if avg_lf >= 80:
        return "Profitable"
    elif avg_lf >= 60:
        return "Break Even"
    else:
        return "Rugi"


def analisis_rute(log):
    # ① Kasus kosong
    if not log:
        return "Tidak ada data penerbangan."

    # ② Akumulasi per rute
    #    key  = (asal.lower(), tujuan.lower())
    #    val  = [asal_title, tujuan_title,
    #             list of (kode, durasi, penumpang, kapasitas)]
    akum = {}

    for kode, asal, tujuan, bgt, tiba, pnp, kap in log:
        key       = (asal.lower(), tujuan.lower())
        durasi    = hitung_durasi(bgt, tiba)
        if key in akum:
            akum[key][2].append((kode, durasi, pnp, kap))
        else:
            akum[key] = [
                asal.title(),
                tujuan.title(),
                [(kode, durasi, pnp, kap)]
            ]

    # ③ Bangun hasil
    hasil = []
    for key, val in akum.items():
        asal_t, tujuan_t, flights = val

        total_pnp = sum(f[2] for f in flights)

        # avg load factor = rata-rata LF tiap penerbangan
        avg_lf = round(
            sum(f[2] / f[3] * 100 for f in flights) / len(flights),
            1
        )

        status = tentukan_status(avg_lf)

        # penerbangan tercepat: durasi min, lalu kode lex min
        tercepat = min(flights, key=lambda f: (f[1], f[0]))
        kode_tc  = tercepat[0]
        dur_tc   = tercepat[1]

        hasil.append(
            ((asal_t, tujuan_t), total_pnp, avg_lf, status, kode_tc, dur_tc)
        )

    # ④ Sort: avg_lf desc → asal asc → tujuan asc
    hasil.sort(key=lambda x: (-x[2], x[0][0], x[0][1]))

    return tuple(hasil)

log = eval(input())
print(analisis_rute(log))