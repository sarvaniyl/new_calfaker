import pytest
from calculator import add, subtract, multiply, divide
from faker import Faker
import random  # Add this import

fake = Faker()

@pytest.mark.parametrize("test_data", [
    {"a": fake.random_int(min=-100, max=100), 
     "b": fake.random_int(min=-100, max=100), 
     "operation": random.choice(["add", "subtract", "multiply", "divide"])}
    for _ in range(10)
])
def test_operations(test_data):
    a, b, operation = test_data["a"], test_data["b"], test_data["operation"]
    
    if operation == "add":
        assert add(a, b) == a + b
    elif operation == "subtract":
        assert subtract(a, b) == a - b
    elif operation == "multiply":
        assert multiply(a, b) == a * b
    elif operation == "divide":
        if b == 0:
            with pytest.raises(ValueError, match="Division by zero is not allowed."):
                divide(a, b)
        else:
            assert divide(a, b) == a / b

def test_addition():
    """Test the addition function with random values."""
    for _ in range(10):
        a, b = fake.random_int(min=-100, max=100), fake.random_int(min=-100, max=100)
        assert add(a, b) == a + b


def test_subtraction():
    """Test that the subtraction function works correctly."""
    assert subtract(2, 2) == 0
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1

def test_multiplication():
    """Test that the multiplication function works correctly."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0
    assert multiply(1, -1) == -1

def test_division():
    """Test that the division function works correctly."""
    assert divide(6, 3) == 2
    assert divide(-8, 4) == -2
    assert divide(10, 5) == 2
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed."
