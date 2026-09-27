"""Regression test: FCFS against the textbook three-process example."""
from scheduler_sim.metrics import compute_metrics
from scheduler_sim.process import Process
from scheduler_sim.schedulers import schedule_fcfs


def test_fcfs_matches_hand_worked_example():
    # P1 arrives at 0.0 with burst 8, P2 arrives at 0.4 with burst 4, P3
    # arrives at 1.0 with burst 1. Under FCFS the completion times are
    # 8, 12, 13, giving turnaround times of 8, 11.6, and 12 -- an average
    # of 10.53 ms.
    procs = [
        Process(pid=1, arrival_time=0.0, burst_time=8.0),
        Process(pid=2, arrival_time=0.4, burst_time=4.0),
        Process(pid=3, arrival_time=1.0, burst_time=1.0),
    ]

    schedule_fcfs(procs)
    m = compute_metrics(procs)

    assert procs[0].finish_time == 8.0
    assert procs[1].finish_time == 12.0
    assert procs[2].finish_time == 13.0
    assert round(m.avg_turnaround_time, 2) == 10.53
