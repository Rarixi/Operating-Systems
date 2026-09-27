# CPU Scheduling Simulator

A CPU scheduling algorithm simulator and benchmark suite implementing and
comparing FCFS, non-preemptive SJF, preemptive SJF (SRTF), non-preemptive
and preemptive Priority scheduling, and Round Robin.

Built for the scheduling-algorithms programming project in *Operating
System Concepts* (Silberschatz, Galvin, & Gagne, 10th ed.).

## Setup

```sh
pip install -r requirements.txt   # pytest + matplotlib (tests and plots only)
```

The simulator itself has no third-party dependencies -- only the standard
library is needed to run `scheduler_sim.main`.

## Run

```sh
python -m scheduler_sim.main workload.csv [quantum]
```

`workload.csv` has one process per line: `pid,arrival_time,burst_time,priority`
(a header row is optional). `quantum` (default 2.0) is used only by Round
Robin. The program runs every algorithm against the workload and prints
each one's average waiting time, turnaround time, response time, CPU
utilization, and throughput.

## Test

```sh
pytest
```

## Benchmark

```sh
python benchmarks/run_benchmarks.py   # writes benchmarks/results/timings.csv
python benchmarks/plot_results.py     # writes benchmarks/results/timings.png
```

`make bench` runs both in one step.

## Layout

```
scheduler_sim/   Process/workload/metrics modules, schedulers/ (one file per algorithm), main.py
tests/           pytest regression tests, checked against hand-worked examples
benchmarks/      Workload generator and scripts that compare algorithm performance
docs/            Design notes
```

See `CODING_STANDARDS.md` for naming, formatting, typing, and testing
conventions used throughout the codebase.
