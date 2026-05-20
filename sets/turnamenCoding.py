from collections import defaultdict

# ── Tiga inverted index ──────────────────────────────────
univ_to_ids  : dict[str, set[int]]       = defaultdict(set)
lang_to_ids  : dict[str, set[int]]       = defaultdict(set)
# univ + lang -> set ID (untuk CARI & RIVAL tanpa intersection ulang)
univ_lang_ids: dict[tuple, set[int]]     = defaultdict(set)
# lang -> set universitas yang punya peserta berkemampuan lang (untuk DOMINAN)
lang_to_univs: dict[str, set[str]]       = defaultdict(set)
# univ -> set lang yang dikuasai pesertanya (untuk JEMBATAN)
univ_to_langs: dict[str, set[str]]       = defaultdict(set)

N, Q = map(int, input().split())

for _ in range(N):
    parts = input().split()
    pid   = int(parts[0])
    univ  = parts[1]
    langs = parts[2:]

    univ_to_ids[univ].add(pid)
    for lang in langs:
        lang_to_ids[lang].add(pid)
        univ_lang_ids[(univ, lang)].add(pid)
        lang_to_univs[lang].add(univ)
        univ_to_langs[univ].add(lang)

def fmt_id(s: set) -> str:
    return " ".join(map(str, sorted(s))) if s else "KOSONG"

def fmt_str(s: set) -> str:
    return " ".join(sorted(s)) if s else "KOSONG"

out = []

for _ in range(Q):
    parts = input().split()
    op    = parts[0]

    if op == "UNIV":
        out.append(fmt_id(univ_to_ids.get(parts[1], set())))

    elif op == "BAHASA":
        out.append(fmt_id(lang_to_ids.get(parts[1], set())))

    elif op == "CARI":
        # langsung lookup index (univ, lang) — O(1)
        out.append(fmt_id(univ_lang_ids.get((parts[1], parts[2]), set())))

    elif op == "RIVAL":
        _, univA, univB, lang = parts
        a = univ_lang_ids.get((univA, lang), set())
        b = univ_lang_ids.get((univB, lang), set())
        out.append(fmt_id(a - b))

    elif op == "DOMINAN":
        maks = max(len(v) for v in lang_to_univs.values())
        dom  = sorted(l for l, v in lang_to_univs.items() if len(v) == maks)
        out.append(" ".join(dom))

    elif op == "JEMBATAN":
        _, univA, univB = parts
        # bahasa yang ada di kedua universitas = intersection set bahasa
        a = univ_to_langs.get(univA, set())
        b = univ_to_langs.get(univB, set())
        out.append(fmt_str(a & b))

print("\n".join(out))