"""Priority scheduling: non-preemptive and preemptive.

Lower priority value means higher priority, matching the textbook's
convention.
"""
import math
from typing import List

from ..process import Process


def schedule_priority_nonpreemptive(procs: List[Process]) -> None:
    remaining = list(procs)
    clock = 0.0

    while remaining:
        ready = [p for p in remaining if p.arrival_time <= clock]
        if not ready:
            clock = min(p.arrival_time for p in remaining)
            continue

        best = min(ready, key=lambda p: (p.priority, p.arrival_time))
        best.start_time = clock
        best.started = True
        clock += best.burst_time
        best.finish_time = clock
        remaining.remove(best)


def schedule_priority_preemptive(procs: List[Process]) -> None:
    for p in procs:
        p.remaining_time = p.burst_time

    clock = 0.0
    remaining = list(procs)

    while remaining:
        ready = [p for p in remaining if p.arrival_time <= clock]
        if not ready:
            clock = min(p.arrival_time for p in remaining)
            continue

        best = min(ready, key=lambda p: p.priority)
        if not best.started:
            best.start_time = clock
            best.started = True

        future_arrivals = [p.arrival_time for p in remaining if p.arrival_time > clock]
        next_arrival = min(future_arrivals) if future_arrivals else math.inf

        run_for = min(best.remaining_time, next_arrival - clock)
        clock += run_for
        best.remaining_time -= run_for

        if best.remaining_time <= 1e-9:
            best.finish_time = clock
            remaining.remove(best)
