# DO NOT EDIT ME

from ..git_workshop import current_year, first_ten_even_integers

def test_current_year():
    assert current_year == 2024

def test_first_ten_even_integers():
    assert first_ten_even_integers() == [2,4,6,8,10,12,14,16,18,20]
