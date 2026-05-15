"""Benchmark suite."""
import time
import hashlib
import logging
from typing import Dict

logger = logging.getLogger("specterhash.benchmark")

class BenchmarkRunner:
    def bench_md5(self, count=1000000) -> Dict:
        start = time.perf_counter()
        for i in range(count):
            hashlib.md5(f"test{i}".encode()).hexdigest()
        elapsed = time.perf_counter() - start
        return {"hash": "md5", "count": count, "elapsed": elapsed, "rate": count/elapsed}

    def bench_sha256(self, count=1000000) -> Dict:
        start = time.perf_counter()
        for i in range(count):
            hashlib.sha256(f"test{i}".encode()).hexdigest()
        elapsed = time.perf_counter() - start
        return {"hash": "sha256", "count": count, "elapsed": elapsed, "rate": count/elapsed}

    def run_all(self):
        return [self.bench_md5(), self.bench_sha256()]

    def print_results(self, results):
        print("\nSPECTERHASH BENCHMARK")
        print("=" * 50)
        for r in results:
            print(f"  {r['hash']:8s} | {r['rate']:,.0f} H/s")
        print("=" * 50)
