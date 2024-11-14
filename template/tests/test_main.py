# DO NOT EDIT ME

from .. import git_workshop as ws
import pytest

# current_year tests
test_function="current_year"
@pytest.mark.skipif(not hasattr(ws, test_function), reason=test_function)
def test_current_year():
    assert ws.current_year() == 2024

# first_n_even_integers tests
test_function="first_n_even_integers"
@pytest.mark.skipif(not hasattr(ws, test_function), reason=test_function)
def test_first_ten_even_integers():
    assert ws.first_n_even_integers(10) == [2,4,6,8,10,12,14,16,18,20]

@pytest.mark.skipif(not hasattr(ws, test_function), reason=test_function)
def test_first_2_even_integers():
    assert ws.first_n_even_integers(2) == [2,4]
