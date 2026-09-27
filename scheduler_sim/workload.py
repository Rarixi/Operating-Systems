"""CSV workload loading for the CPU scheduling simulator."""
import csv
import sys
from typing import List

from .process import Process


def load_workload(path: str) -> List[Process]:
    """Loads a CSV workload with columns: pid,arrival_time,burst_time,priority.

    A header row is optional and detected automatically. A malformed row is
    reported to stderr and skipped rather than raising.
    """
    processes: List[Process] = []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for line_no, row in enumerate(reader, start=1):
            if not row or row[0].strip().startswith("#"):
                continue
            if line_no == 1 and row[0].strip().lower() == "pid":
                continue
            try:
                pid = int(row[0])
                arrival = float(row[1])
                burst = float(row[2])
                priority = int(row[3]) if len(row) > 3 and row[3].strip() != "" else 0
            except (ValueError, IndexError):
                print(f"load_workload: skipping malformed line {line_no}", file=sys.stderr)
                continue
            processes.append(
                Process(pid=pid, arrival_time=arrival, burst_time=burst, priority=priority)
            )
    return processes
