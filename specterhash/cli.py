"""CLI for specterhash."""
import argparse
import logging
import sys

def main():
    parser = argparse.ArgumentParser(prog="specterhash", description="Crypto auditing tool")
    sub = parser.add_subparsers(dest="command")

    audit = sub.add_parser("audit", help="Audit password strength")
    audit.add_argument("--input", "-i", required=True)
    audit.add_argument("--rules", default="nist")

    recover = sub.add_parser("recover", help="Recover hashes")
    recover.add_argument("--hash", required=True)
    recover.add_argument("--target", required=True)
    recover.add_argument("--wordlist", required=True)

    entropy = sub.add_parser("entropy", help="Analyze entropy")
    entropy.add_argument("--input", "-i", required=True)

    args = parser.parse_args()
    if not args.command: parser.print_help(); sys.exit(1)
    logging.basicConfig(level=logging.INFO)

    if args.command == "audit":
        from .compliance import ComplianceChecker
        checker = ComplianceChecker()
        result = checker.audit_file(args.input)
        print(f"Compliant: {result['compliant']}/{result['total']}")

    elif args.command == "entropy":
        from .entropy import EntropyAnalyzer
        analyzer = EntropyAnalyzer()
        with open(args.input) as f:
            passwords = [l.strip() for l in f if l.strip()]
        result = analyzer.analyze_batch(passwords)
        print(f"Average entropy: {result['avg_entropy']:.1f} bits")
        print(f"Weak passwords: {result['weak_count']}/{result['total']}")

if __name__ == "__main__": main()
