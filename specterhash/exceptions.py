"""Exceptions."""

class SpecterHashError(Exception): pass
class AuditError(SpecterHashError): pass
class ComplianceError(SpecterHashError): pass
class HashError(SpecterHashError): pass
class GPUError(SpecterHashError): pass
