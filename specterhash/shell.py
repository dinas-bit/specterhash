"""Interactive shell for specterhash."""
import cmd
import logging

logger = logging.getLogger("specterhash.shell")

class SpecterShell(cmd.Cmd):
    prompt = "specterhash> "
    intro = "SpecterHash Interactive Shell. Type help for commands."

    def do_audit(self, arg):
        """Audit a password: audit <password>"""
        from .entropy import EntropyAnalyzer
        a = EntropyAnalyzer()
        r = a.analyze(arg)
        print(f"Entropy: {r['entropy_bits']} bits | Strength: {r['strength']}")

    def do_check(self, arg):
        """Check NIST compliance: check <password>"""
        from .compliance import ComplianceChecker
        c = ComplianceChecker()
        r = c.check_nist(arg)
        print(f"Compliant: {r['compliant']} | Score: {r['score']}")

    def do_generate(self, arg):
        """Generate password: generate [length]"""
        from .generator import PasswordGenerator
        length = int(arg) if arg else 16
        g = PasswordGenerator(length=length)
        print(g.generate())

    def do_quit(self, arg):
        return True

def run_shell():
    SpecterShell().cmdloop()
