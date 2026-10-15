from collections import Counter


def isAnagram_dict(s: str, t: str) -> bool:
    d = {}
    v = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    for j in t:
        v[j] = v.get(j, 0) + 1
    return v == d


def isAnagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
