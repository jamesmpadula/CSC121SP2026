#James Padula
#4/28/2026
#CSC-121-OA1

import pytest 
from employee import Employee

@pytest.fixture
def example_employee():
    return Employee('James', 'Pad', 50000)

def test_give_default_raise(example_employee):
    example_employee.give_raise()
    assert example_employee.salary == 55000

def test_give_custom_raise(example_employee):
    example_employee.give_raise(10000)
    assert example_employee.salary == 60000