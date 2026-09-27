#!/usr/bin/env python3
"""Benchmarks each scheduling algorithm's wall-clock time across a range of
workload sizes and writes the results to benchmarks/results/timings.csv."""
import csv
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from generate_workload import generate  # noqa: E402 (needs sys.path set up first)

from scheduler_sim.process import Process  # noqa: E402
from scheduler_sim.schedulers import (  # noqa: E402
    schedule_fcfs,
    schedule_priority_nonpreemptive,
    schedule_priority_preemptive,
    schedule_rr,
    schedule_sjf_nonpreemptive,
    schedule_srtf,
)

SIZES = [10, 50, 100, 500, 1000, 5000]

ALGORITHMS = {
    "fcfs": schedule_fcfs,
    "sjf_nonpreemptive": schedule_sjf_nonpreemptive,
    "srtf": schedule_srtf,
    "priority_nonpreemptive": schedule_priority_nonpreemptive,
    "priority_preemptive": schedule_priority_preemptive,
    "round_robin": lambda procs: schedule_rr(procs, 2.0),
}


def make_processes(rows):
    return [Process(pid=pid, arrival_time=a, burst_time=b, priority=pr) for pid, a, b, pr in rows]


def main():
    results_dir = Path(__file__).resolve().parent / "results"
    results_dir.mkdir(exist_ok=True)

    with open(results_dir / "timings.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["num_processes", "algorithm", "wall_clock_seconds"])

        for size in SIZES:
            rows = generate(size, seed=42)
            for name, schedule_fn in ALGORITHMS.items():
                procs = make_processes(rows)
                start = time.perf_counter()
                schedule_fn(procs)
                elapsed = time.perf_counter() - start
                writer.writerow([size, name, f"{elapsed:.6f}"])
                print(f"n={size:>5}  {name:<24} {elapsed:.4f}s")

    print(f"Results written to {results_dir / 'timings.csv'}")


if __name__ == "__main__":
    main()
