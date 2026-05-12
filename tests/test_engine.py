import pytest
from specterhash.engine import AuditEngine
from specterhash.hash_types import HashType

class TestEngine:
    def test_verify_md5(self):
        import hashlib
        engine = AuditEngine()
        h = hashlib.md5(b"test").hexdigest()
        assert engine.verify_hash("test", h, HashType.MD5)

    def test_verify_wrong(self):
        engine = AuditEngine()
        assert not engine.verify_hash("wrong", "d41d8cd98f00b204e9800998ecf8427e", HashType.MD5)
