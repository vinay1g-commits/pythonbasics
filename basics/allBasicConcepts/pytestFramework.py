"""
 popular testing framework for Python that makes it easy to write simple
 and scalable test cases

Simple Syntax: Tests are written as functions prefixed with test_,
which makes it straightforward to create and run tests.
Fixtures: Provides a way to set up test environments and share code
between tests.
Parametrization: Allows running the same test with different parameters.
Assertions: Uses plain assert statements for testing conditions.
Plugins: Extensible with a wide range of plugins available for various functionalities.
"""
import pytest


def add(a,b):
    return a+b

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

@pytest.fixture
def sample_data():
    return [1,2,3]

def test_sum(sample_data):
    assert sum(sample_data) == 6

def test_length(sample_data):
    assert len(sample_data) == 3

@pytest.mark.parametrize("input1, input2, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(input1, input2, expected):
    assert add(input1, input2) == expected

def divide(a,b):
    return a/b

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1,0)