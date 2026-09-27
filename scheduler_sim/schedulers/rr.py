"""Round Robin scheduling."""
from collections import deque
from typing import List

from ..process import Process


def schedule_rr(procs: List[Process], quantum: float = 2.0) -> None:
    for p in procs:
        p.remaining_time = p.burst_time

    order = sorted(procs, key=lambda p: p.arrival_time)
    queue = deque()
    clock = 0.0
    next_to_admit = 0
    completed = 0
    n = len(procs)

    def admit_arrivals() -> None:
        nonlocal next_to_admit
        while next_to_admit < n and order[next_to_admit].arrival_time <= clock:
            queue.append(order[next_to_admit])
            next_to_admit += 1

    admit_arrivals()
    if not queue and next_to_admit < n:
        clock = order[next_to_admit].arrival_time
        admit_arrivals()

    while completed < n:
        p = queue.popleft()

        if not p.started:
            p.start_time = clock
            p.started = True

        run_for = min(p.remaining_time, quantum)
        clock += run_for
        p.remaining_time -= run_for

        # newly arrived processes join the queue before the just-run one
        # rejoins it, which is the standard Round Robin tie-break rule
        admit_arrivals()

        if p.remaining_time <= 1e-9:
            p.finish_time = clock
            completed += 1
        else:
            queue.append(p)

        if not queue and completed < n and next_to_admit < n:
            clock = order[next_to_admit].arrival_time
            admit_arrivals()
