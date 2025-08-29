import pytest
from operation import Operation

@pytest.mark.parametrize("given, expected", [
    (42424200, 42424200),
    (-42424200, -42424200),
    (4, 4),
    (-4, -4)
])
def test_construct_cents(given: int, expected: int) -> None:
    t = Operation(given, "anything")
    assert t.cents == expected

@pytest.mark.parametrize("given, expected", [
    ("anything", "anything"),
    ("hello", "hello"),
    ('a', 'a')
])
def test_construct_description(given: str, expected: str) -> None:
    t = Operation(424242, given)
    assert t.description == expected

@pytest.mark.parametrize("given, expected", [
    (42424200, "credit"),
    (-42424200, "debit"),
    (4, "credit"),
    (-4, "debit")
])
def test_construct_operation_type(given: int, expected: str) -> None:
    t = Operation(given, "anything")
    assert t.operation_type == expected

def test_construct_operation_type_with_zero() -> None:
    with pytest.raises(ValueError):
        t = Operation(0, "anything")
