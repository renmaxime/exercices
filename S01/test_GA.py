from group_anagram import groupAnagrams


def test_groupanagramme():
    resultat = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    attendu = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert sorted(sorted(g) for g in resultat) == sorted(sorted(g) for g in attendu)


def test_chaine_vide():
    assert groupAnagrams([""]) == [[""]]
