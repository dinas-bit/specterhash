import pytest
from specterhash.entropy import EntropyAnalyzer

class TestEntropy:
    def test_weak_password(self):
        a = EntropyAnalyzer()
        r = a.analyze("123456")
        assert r["strength"] in ["Very Weak", "Weak"]

    def test_strong_password(self):
        a = EntropyAnalyzer()
        r = a.analyze("C0mpl3x!P@ssw0rd#2024")
        assert r["entropy_bits"] > 60

    def test_batch(self):
        a = EntropyAnalyzer()
        r = a.analyze_batch(["abc", "XYZ123!", "Tr0ub4dor&3horse"])
        assert r["total"] == 3
