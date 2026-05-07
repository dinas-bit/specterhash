# 👻 SpecterHash

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Cryptographic auditing and password recovery tool with GPU-accelerated hash operations on AMD ROCm.

## What It Does

SpecterHash audits password strength, recovers lost credentials, and analyzes cryptographic implementations. Built for security professionals who need fast hash verification and compliance checking.

## Key Features

- **Password audit** — Check password databases against breach lists
- **Hash recovery** — GPU-accelerated recovery for MD5, SHA, bcrypt, Argon2
- **Entropy analysis** — Measure password strength and randomness
- **Compliance checking** — NIST SP 800-63B password guidelines
- **Batch verification** — Verify millions of hashes per second
- **Real-time dashboard** — Live hashrate, temperature, GPU utilization

## Quick Start

```bash
git clone https://github.com/dinas-bit/specterhash.git
cd specterhash
pip install -r requirements.txt
specterhash audit --input passwords.txt --rules nist
specterhash recover --hash md5 --target hashes.txt --wordlist rockyou.txt
```

## Ecosystem

| Repo | Role |
|------|------|
| [vulcan-crypt](https://github.com/dinas-bit/vulcan-crypt) | Hash cracking |
| [zkforge](https://github.com/dinas-bit/zkforge) | ZKP acceleration |
| [latticeforge](https://github.com/dinas-bit/latticeforge) | Post-quantum crypto |

## License

Apache 2.0
