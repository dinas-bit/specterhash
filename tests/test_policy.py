import pytest
from specterhash.policy import PolicyEngine, PasswordPolicy

class TestPolicy:
    def test_short_password(self):
        engine = PolicyEngine()
        r = engine.check("abc")
        assert not r["pass"]

    def test_good_password(self):
        engine = PolicyEngine()
        r = engine.check("MyS3cure!Pass")
        assert r["pass"]

    def test_custom_policy(self):
        policy = PasswordPolicy(min_length=4, require_special=False)
        engine = PolicyEngine(policy)
        assert engine.check("abc1").get("pass", False) or len(engine.check("abc1")["violations"]) == 0
