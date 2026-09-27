#!/usr/bin/env python3
"""Generate a random CPU-scheduling workload CSV file.

Usage: generate_workload.py <num_processes> <output.csv> [--seed N]
"""
import argparse
import random
from typing import List, Optional, Tuple


def generate(num_processes: int, seed: Optional[int] = None) -> List[Tuple[int, float, float, int]]:
    rng = random.Random(seed)
    rows = []
    clock = 0.0
    for pid in range(1, num_processes + 1):
        clock += rng.uniform(0, 3)
        arrival = round(clock, 1)
        burst = round(rng.uniform(1, 20), 1)
        priority = rng.randint(1, 5)
        rows.append((pid, arrival, burst, priority))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("num_processes", type=int)
    parser.add_argument("output", help="path to the CSV file to write")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    rows = generate(args.num_processes, args.seed)
    with open(args.output, "w") as f:
        f.write("pid,arrival_time,burst_time,priority\n")
        for pid, arrival, burst, priority in rows:
            f.write(f"{pid},{arrival},{burst},{priority}\n")

    print(f"Wrote {len(rows)} processes to {args.output}")


if __name__ == "__main__":
    main()
