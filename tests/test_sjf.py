"""Regression test: non-preemptive SJF against the textbook example.

Same three processes as test_fcfs.py. At t=8 (when P1 finishes), both P2
(burst 4) and P3 (burst 1) are available, so SJF runs P3 first, then P2.
"""
from scheduler_sim.metrics import compute_metrics
from scheduler_sim.process import Process
from scheduler_sim.schedulers import schedule_sjf_nonpreemptive


def test_sjf_matches_hand_worked_example():
    procs = [
        Process(pid=1, arrival_time=0.0, burst_time=8.0),
        Process(pid=2, arrival_time=0.4, burst_time=4.0),
        Process(pid=3, arrival_time=1.0, burst_time=1.0),
    ]

    schedule_sjf_nonpreemptive(procs)
    m = compute_metrics(procs)

    by_pid = {p.pid: p for p in procs}
    assert by_pid[1].finish_time == 8.0
    assert by_pid[3].finish_time == 9.0
    assert by_pid[2].finish_time == 13.0
    assert round(m.avg_turnaround_time, 2) == 9.53
