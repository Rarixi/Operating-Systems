"""Shortest-Job-First scheduling: non-preemptive and preemptive (SRTF)."""
import math
from typing import List

from ..process import Process


def schedule_sjf_nonpreemptive(procs: List[Process]) -> None:
    remaining = list(procs)
    clock = 0.0

    while remaining:
        ready = [p for p in remaining if p.arrival_time <= clock]
        if not ready:
            clock = min(p.arrival_time for p in remaining)
            continue

        best = min(ready, key=lambda p: (p.burst_time, p.arrival_time))
        best.start_time = clock
        best.started = True
        clock += best.burst_time
        best.finish_time = clock
        remaining.remove(best)


def schedule_srtf(procs: List[Process]) -> None:
    """Preemptive SJF, modeled as a discrete-event simulation that only
    stops the clock at arrivals and completions, so it stays exact
    regardless of burst-time granularity."""
    for p in procs:
        p.remaining_time = p.burst_time

    clock = 0.0
    remaining = list(procs)

    while remaining:
        ready = [p for p in remaining if p.arrival_time <= clock]
        if not ready:
            clock = min(p.arrival_time for p in remaining)
            continue

        best = min(ready, key=lambda p: p.remaining_time)
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
