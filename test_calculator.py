import pytest
import calculator
from calculator import *


def test_add():
    assert add(4,5) == 9

def test_subtract():
    assert subtract(6,2) == 4

def test_multiply():
    assert multiply(2,11) == 22

def test_div():
    assert divide(10,2) == 5

@pytest.mark.parametrize("num1,num2,expectedRes", [(1,2,2),(3,4,12),(5,6,30)])
def test_param_multi(num1,num2,expectedRes):
    result = calculator.multiply(num1,num2)
    assert result == expectedRes

