import pytest
from principal import somar


def test_somar():
    assert somar(2, 4) == 6
