"""One module per scheduling algorithm, all sharing the same signature:
a scheduler mutates a list of Process objects in place, setting start_time
and finish_time (and remaining_time, for preemptive ones) on each."""
from .fcfs import schedule_fcfs
from .priority import schedule_priority_nonpreemptive, schedule_priority_preemptive
from .rr import schedule_rr
from .sjf import schedule_sjf_nonpreemptive, schedule_srtf

__all__ = [
    "schedule_fcfs",
    "schedule_sjf_nonpreemptive",
    "schedule_srtf",
    "schedule_priority_nonpreemptive",
    "schedule_priority_preemptive",
    "schedule_rr",
]
