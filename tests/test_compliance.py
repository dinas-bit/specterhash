import pytest
from specterhash.compliance import ComplianceChecker

class TestCompliance:
    def test_short_password(self):
        c = ComplianceChecker()
        r = c.check_nist("abc")
        assert not r["compliant"]
        assert any("short" in i.lower() for i in r["issues"])

    def test_good_password(self):
        c = ComplianceChecker()
        r = c.check_nist("MyS3cure!Pass2024")
        assert r["compliant"]
