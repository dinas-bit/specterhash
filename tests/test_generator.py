import pytest
from specterhash.generator import PasswordGenerator

class TestGenerator:
    def test_generate_length(self):
        g = PasswordGenerator(length=20)
        assert len(g.generate()) == 20

    def test_generate_batch(self):
        g = PasswordGenerator()
        batch = g.generate_batch(10)
        assert len(batch) == 10
        assert len(set(batch)) == 10  # All unique

    def test_passphrase(self):
        g = PasswordGenerator()
        pp = g.generate_passphrase(4)
        assert pp.count("-") == 3
