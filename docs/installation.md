# Installation

## Requirements
- Python 3.10+
- AMD GPU (optional, for GPU acceleration)

```bash
git clone https://github.com/dinas-bit/specterhash.git
cd specterhash
pip install -r requirements.txt
specterhash --help
```

## Docker

```bash
docker build -t specterhash .
docker run specterhash audit --input passwords.txt
```
