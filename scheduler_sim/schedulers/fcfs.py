"""First-Come, First-Served scheduling."""
from typing import List

from ..process import Process


def schedule_fcfs(procs: List[Process]) -> None:
    procs.sort(key=lambda p: (p.arrival_time, p.pid))

    clock = 0.0
    for p in procs:
        clock = max(clock, p.arrival_time)
        p.start_time = clock
        p.started = True
        clock += p.burst_time
        p.finish_time = clock
