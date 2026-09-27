.PHONY: test run bench clean

test:
	python -m pytest -q

run:
	python -m scheduler_sim.main $(WORKLOAD) $(QUANTUM)

bench:
	python benchmarks/run_benchmarks.py
	python benchmarks/plot_results.py

clean:
	find . -name '__pycache__' -type d -exec rm -rf {} +
	rm -rf .pytest_cache benchmarks/results
