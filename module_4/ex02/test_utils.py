import pytest
from  utils import format_cents

@pytest.mark.parametrize("given, expected", [
    (11_222_00, "[+] R$ 11.222,00"),
    (-11_222_00, "[-] R$ 11.222,00"),
    (42_442_442_42, "[+] R$ 42.442.442,42"),
    (-42_442_442_42, "[-] R$ 42.442.442,42"),
    (0, "[-] R$ 0,00"),
])
def test_format_cents(given: int , expected: str) -> None:
    assert format_cents(given) == expected
