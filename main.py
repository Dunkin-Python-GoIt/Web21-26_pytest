import allure
import pytest

def add_two_numbers(a: int, b: int) -> int:
    """Add two numbers

    Args:
        a (int): first argument
        b (int): second argument

    Returns:
        int: _description_
    """    
    return a + b


def test_add_numbers():
    assert add_two_numbers(1, 1) == 3


@pytest.fixture
def prepare_data():
    return 1, 2


# @pytest.mark.skip(reason="main")
@allure.title("My New tests")
def test_add_negative_numbers(prepare_data):
    assert add_two_numbers(prepare_data[0], prepare_data[1]) == 2 