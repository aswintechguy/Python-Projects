import pytest
from hackers_realm import operations

def test_addition():
    assert operations.add(2, 3) == 5
    assert operations.add(5, 5) == 10

def test_subtraction():
    assert operations.subtract(5, 4) == 1