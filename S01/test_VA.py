from valid_anagram import isAnagram

def test_anagramme():
    assert isAnagram("anagram", "nagaram") is True

def test_pas_anagramme():
    assert isAnagram("rat", "car") is False