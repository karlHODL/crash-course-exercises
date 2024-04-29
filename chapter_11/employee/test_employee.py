import pytest
from employee import Employee

@pytest.fixture
def employee():
    """A sample employee instance."""
    return Employee('john', 'doe', 50000)

def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    employee.give_raise()
    assert employee.salary == 55000

def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    employee.give_raise(10000)
    assert employee.salary == 60000