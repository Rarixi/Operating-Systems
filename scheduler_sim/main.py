"""Command-line driver: runs every scheduling algorithm against a workload
and reports each one's metrics."""
import argparse
import copy
import sys
from typing import Callable, List

from .metrics import compute_metrics, print_metrics
from .process import Process
from .schedulers import (
    schedule_fcfs,
    schedule_priority_nonpreemptive,
    schedule_priority_preemptive,
    schedule_rr,
    schedule_sjf_nonpreemptive,
    schedule_srtf,
)
from .workload import load_workload

DEFAULT_QUANTUM = 2.0


def run_and_report(
    name: str, workload: List[Process], schedule_fn: Callable[[List[Process]], None]
) -> None:
    procs = copy.deepcopy(workload)
    schedule_fn(procs)
    print_metrics(compute_metrics(procs), name)


def main(argv: List[str] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compare CPU scheduling algorithms on a workload."
    )
    parser.add_argument("workload", help="CSV file: pid,arrival_time,burst_time,priority")
    parser.add_argument(
        "quantum", nargs="?", type=float, default=DEFAULT_QUANTUM,
        help="Round Robin time quantum (default: 2.0)",
    )
    args = parser.parse_args(argv)

    workload = load_workload(args.workload)
    if not workload:
        print(f"Failed to load a workload from '{args.workload}'", file=sys.stderr)
        return 1

    print(f"Loaded {len(workload)} processes from {args.workload}")

    run_and_report("FCFS", workload, schedule_fcfs)
    run_and_report("SJF (non-preemptive)", workload, schedule_sjf_nonpreemptive)
    run_and_report("SRTF (preemptive SJF)", workload, schedule_srtf)
    run_and_report("Priority (non-preemptive)", workload, schedule_priority_nonpreemptive)
    run_and_report("Priority (preemptive)", workload, schedule_priority_preemptive)
    run_and_report(
        f"Round Robin (q={args.quantum:.1f})", workload,
        lambda procs: schedule_rr(procs, args.quantum),
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
