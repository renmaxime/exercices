from contains_duplicate import containsDuplicate

def test_duplicate():
    assert containsDuplicate([1,2,3,1]) is True

def test_pas_duplicate():
    assert containsDuplicate([1,2,3,4]) is False