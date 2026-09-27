#!/usr/bin/env python3
"""Plot benchmarks/results/timings.csv: workload size vs. wall-clock time,
one line per algorithm.

Usage: plot_results.py [timings.csv] [output.png]
"""
import csv
import sys
from collections import defaultdict


def main(path="benchmarks/results/timings.csv", out="benchmarks/results/timings.png"):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        sys.exit("matplotlib is required: pip install matplotlib")

    series = defaultdict(list)
    with open(path) as f:
        for row in csv.DictReader(f):
            series[row["algorithm"]].append(
                (int(row["num_processes"]), float(row["wall_clock_seconds"]))
            )

    plt.figure(figsize=(7.5, 4.5))
    for name, points in series.items():
        points.sort()
        sizes = [pt[0] for pt in points]
        times = [pt[1] for pt in points]
        plt.plot(sizes, times, marker="o", label=name)

    plt.xlabel("Number of processes")
    plt.ylabel("Wall-clock time (s)")
    plt.title("Scheduling algorithm runtime vs. workload size")
    plt.legend(fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out)
    print(f"Saved plot to {out}")


if __name__ == "__main__":
    main(*sys.argv[1:])
