# Coding Standards

These conventions apply to all Python source in `scheduler_sim/`,
`tests/`, and `benchmarks/`.

## Naming

- Functions, variables, and modules: `snake_case` (`schedule_fcfs`, `remaining_time`).
- Classes: `PascalCase` (`Process`, `Metrics`).
- Constants: `UPPER_SNAKE_CASE` (`DEFAULT_QUANTUM`).
- One algorithm per module, named after the algorithm (`fcfs.py`, `sjf.py`, `rr.py`), collected under `scheduler_sim/schedulers/`.

## Formatting

- Follows [PEP 8]: 4-space indentation, lines wrapped at 100 characters.
- Type hints on every function signature (`def schedule_fcfs(procs: List[Process]) -> None:`).
- `@dataclass` for plain data holders (`Process`, `Metrics`) instead of hand-written `__init__`s.
- Formatted with `black`; linted with `ruff` (or `flake8`) before merging, if installed.

## Documentation

- Every module opens with a one-line docstring describing its responsibility.
- Every public function has a docstring stating what it does and what it assumes about its inputs.
- Non-obvious logic (e.g., the discrete-event stepping in `sjf.schedule_srtf`) gets an inline comment explaining *why*, not just *what*.

## Error handling

- `workload.load_workload` reports a malformed CSV row to stderr and skips it rather than raising.
- Library functions raise on truly invalid state (e.g., an empty workload) rather than failing silently; only `main.py`'s CLI entry point catches exceptions to produce a clean exit code.

## Testing

- `pytest` for all tests; test files mirror the module they cover (`test_fcfs.py` tests `schedulers/fcfs.py`).
- Every algorithm has at least one regression test checked against a hand-worked example.
- `pytest` must pass before a branch is merged into `main`.

[PEP 8]: https://peps.python.org/pep-0008/
