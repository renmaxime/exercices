from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    d = defaultdict(list)
    for i in strs:
        cle = "".join(sorted(i))
        d[cle].append(i)
    return list(d.values())
