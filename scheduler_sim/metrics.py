"""Metrics computation for a completed scheduling run."""
from dataclasses import dataclass
from typing import List

from .process import Process


@dataclass
class Metrics:
    avg_waiting_time: float = 0.0
    avg_turnaround_time: float = 0.0
    avg_response_time: float = 0.0
    total_time: float = 0.0      # makespan: last finish time - earliest arrival
    cpu_utilization: float = 0.0  # percent of total_time the CPU was busy
    throughput: float = 0.0       # processes completed per unit time


def compute_metrics(procs: List[Process]) -> Metrics:
    """Derives waiting_time, turnaround_time, and response_time for every
    process from the arrival/start/finish times a scheduler already set,
    then aggregates them into whole-run metrics."""
    n = len(procs)
    if n == 0:
        return Metrics()

    for p in procs:
        p.turnaround_time = p.finish_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time
        p.response_time = p.start_time - p.arrival_time

    earliest_arrival = min(p.arrival_time for p in procs)
    latest_finish = max(p.finish_time for p in procs)
    total_burst = sum(p.burst_time for p in procs)
    total_time = latest_finish - earliest_arrival

    return Metrics(
        avg_waiting_time=sum(p.waiting_time for p in procs) / n,
        avg_turnaround_time=sum(p.turnaround_time for p in procs) / n,
        avg_response_time=sum(p.response_time for p in procs) / n,
        total_time=total_time,
        cpu_utilization=(total_burst / total_time * 100.0) if total_time > 0 else 0.0,
        throughput=(n / total_time) if total_time > 0 else 0.0,
    )


def print_metrics(m: Metrics, algorithm_name: str) -> None:
    print(f"\n--- {algorithm_name} ---")
    print(f"Average waiting time:    {m.avg_waiting_time:.2f}")
    print(f"Average turnaround time: {m.avg_turnaround_time:.2f}")
    print(f"Average response time:   {m.avg_response_time:.2f}")
    print(f"CPU utilization:         {m.cpu_utilization:.2f}%")
    print(f"Throughput:              {m.throughput:.4f} proc/unit time")
