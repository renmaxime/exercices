import pytest

from valid_anagram import isAnagram_counter, isAnagram_dict


@pytest.mark.parametrize("isAnagram", [isAnagram_dict, isAnagram_counter])
def test_anagramme(isAnagram):
    assert isAnagram("anagram", "nagaram") is True


@pytest.mark.parametrize("isAnagram", [isAnagram_dict, isAnagram_counter])
def test_pas_anagramme(isAnagram):
    assert isAnagram("rat", "car") is False
