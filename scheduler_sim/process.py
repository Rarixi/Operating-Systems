"""Process data model for the CPU scheduling simulator."""
from dataclasses import dataclass


@dataclass
class Process:
    """A single simulated process, plus the fields a scheduler and the
    metrics module fill in as it runs."""

    pid: int
    arrival_time: float
    burst_time: float
    priority: int = 0

    # filled in by whichever scheduler runs the workload
    remaining_time: float = 0.0
    start_time: float = 0.0
    finish_time: float = 0.0
    started: bool = False

    # derived by metrics.compute_metrics()
    waiting_time: float = 0.0
    turnaround_time: float = 0.0
    response_time: float = 0.0

    def __post_init__(self) -> None:
        if not self.remaining_time:
            self.remaining_time = self.burst_time
