from collections import defaultdict

def main():
    N, M = map(int, input().split())

    # inverted index: keahlian -> set ID agen
    skill_to_agents: dict[str, set[int]] = defaultdict(set)
    # forward index: ID agen -> set keahlian
    agent_to_skills: dict[int, set[str]] = {}

    for _ in range(N):
        parts = input().split()
        aid   = int(parts[0])
        skills = parts[1:]
        agent_to_skills[aid] = set(skills)
        for sk in skills:
            skill_to_agents[sk].add(aid)

    out = []

    for _ in range(M):
        parts = input().split()
        op    = parts[0]

        if op == "MISI":
            keys = parts[1:]
            # intersection berantai: mulai dari set terkecil (optimasi)
            sets = sorted(
                (skill_to_agents.get(k, set()) for k in keys),
                key=len
            )
            result: set[int] = sets[0].copy()
            for s in sets[1:]:
                result &= s
                if not result:   # early exit
                    break
            if result:
                out.append(" ".join(map(str, sorted(result))))
            else:
                out.append("TIDAK ADA")

        elif op == "LANGKA":
            # cari jumlah minimum, lalu kumpulkan semua keahlian yang seri
            min_count = min(len(v) for v in skill_to_agents.values())
            langka = sorted(
                k for k, v in skill_to_agents.items()
                if len(v) == min_count
            )
            out.append(" ".join(langka))

        elif op == "EKSKLUSIF":
            k = parts[1]
            candidates = skill_to_agents.get(k, set())
            # hitung agen yang HANYA punya keahlian k (set-nya berukuran 1)
            count = sum(
                1 for aid in candidates
                if len(agent_to_skills[aid]) == 1
            )
            out.append(str(count))

        elif op == "BERSAMA":
            keys = parts[1:]
            # langkah 1: intersection berantai (sama seperti MISI)
            sets = sorted(
                (skill_to_agents.get(k, set()) for k in keys),
                key=len
            )
            result = sets[0].copy()
            for s in sets[1:]:
                result &= s
                if not result:
                    break

            if not result:
                out.append("TIDAK ADA")
            else:
                # langkah 2: union semua keahlian agen hasil intersection
                union_skills: set[str] = set()
                for aid in result:
                    union_skills |= agent_to_skills[aid]
                # langkah 3: buang keahlian yang sudah ada di kueri
                extra = union_skills - set(keys)
                if extra:
                    out.append(" ".join(sorted(extra)))
                else:
                    out.append("TIDAK ADA")

    print("\n".join(out))

main()