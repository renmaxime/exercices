
def groupAnagrams(strs: list[str]) -> list[list[str]]:
        d={}
        for i in strs:
            cle = "".join(sorted(i))
            if cle not in d:
                d[cle] = []
            d[cle].append(i)
        return list(d.values())


        