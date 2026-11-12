import pytest

from validate_phonenumber import valider_telefonnummer

@pytest.mark.parametrize(
    "telefonnummer, forventet",
    [
        ("22 11 44 55", True),
        ("11223344", True),
        ("1234abcd", False),
        ("abcd1234", False),
        ("ab cd 12 34", False),
        ("1234567", False),
        ("1234567899", False),
        ("111111111111", False),
    ],
)
def test_mange_telefonnumrer(telefonnummer, forventet):
    assert valider_telefonnummer(telefonnummer) == forventet