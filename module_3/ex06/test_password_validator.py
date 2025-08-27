import pytest
from password_validator import is_valid_password

@pytest.mark.parametrize("password,expected", [
    ("Abcdef1!", True),
    ("Python3.9", True),
    ("ValidPass1@", True),
    ("short1!", False),
    ("PasswordIsTooLong1!", False),
    ("nouppercase1!", False),
    ("NOLOWERCASE1!", False),
    ("NoDigit!!", False),
    ("NoSpecial123", False),
    ("Has Space1!", False),
])
def test_is_valid_password(password, expected):
   assert is_valid_password(password) == expected