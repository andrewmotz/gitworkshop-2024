# DO NOT EDIT ME

from .. import git_workshop as ws
import pytest

# current_year tests
test_function="current_year_workshop"
@pytest.mark.skipif(not hasattr(ws, test_function), reason=f"{test_function} is not defined in git_workshop.py")
def test_current_year_workshop():
    assert ws.current_year_workshop() == 2024

# first_n_even_integers tests
test_function="first_n_even_integers"
@pytest.mark.skipif(not hasattr(ws, test_function), reason=f"{test_function} is not defined in git_workshop.py")
def test_first_ten_even_integers():
    assert ws.first_n_even_integers(10) == [2,4,6,8,10,12,14,16,18,20]

@pytest.mark.skipif(not hasattr(ws, test_function), reason=f"{test_function} is not defined in git_workshop.py")
def test_first_2_even_integers():
    assert ws.first_n_even_integers(2) == [2,4]

# first_n_fibonacci
test_function="first_n_fibonacci"
@pytest.mark.skipif(not hasattr(ws, test_function), reason=f"{test_function} is not defined in git_workshop.py")
def test_first_2_fibonacci():
    assert ws.first_n_fibonacci(2) == [1,1]

@pytest.mark.skipif(not hasattr(ws, test_function), reason=f"{test_function} is not defined in git_workshop.py")
def test_first_1_fibonacci():
    assert ws.first_n_fibonacci(1) == [1]

@pytest.mark.skipif(not hasattr(ws, test_function), reason=f"{test_function} is not defined in git_workshop.py")
def test_first_0_fibonacci():
    assert ws.first_n_fibonacci(0) == []

@pytest.mark.skipif(not hasattr(ws, test_function), reason=f"{test_function} is not defined in git_workshop.py")
def test_first_10_fibonacci():
    assert ws.first_n_fibonacci(2) == [1,1,2,3,5,8,13,21,34,55]
