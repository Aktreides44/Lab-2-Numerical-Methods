import csv
import os
import statistics
import time

SIZES = [1_000, 10_000, 100_000, 1_000_000]
WARMUPS = 5
REPEATS = 10


def calculate_sum(n, reverse=False):
    total = 0.0

    if reverse:
        indices = range(n, 0, -1)
    else:
        indices = range(1, n + 1)

    for k in indices:
        x = float(k)
        total += 1.0 / (x * x)

    return total


os.makedirs("results", exist_ok=True)
csv_path = "results/timing_python.csv"

with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "language", "order", "n", "run",
        "batch_size", "per_call_ms", "returned_sum"
    ])

    print("TASK 4: PYTHON BENCHMARK")
    print(f"Warm-ups: {WARMUPS}, timed runs: {REPEATS}\n")

    for n in SIZES:
        for reverse in [False, True]:
            order = "reverse" if reverse else "forward"

            # Warm-up calls are not timed or recorded.
            for _ in range(WARMUPS):
                calculate_sum(n, reverse)

            times_ms = []
            result = None

            # Each timed run measures one complete summation.
            for run in range(1, REPEATS + 1):
                start = time.perf_counter()
                result = calculate_sum(n, reverse)
                end = time.perf_counter()

                elapsed_ms = (end - start) * 1000.0
                times_ms.append(elapsed_ms)

                writer.writerow([
                    "Python", order, n, run,
                    1, f"{elapsed_ms:.9f}", repr(result)
                ])

            median_ms = statistics.median(times_ms)
            min_ms = min(times_ms)
            max_ms = max(times_ms)

            print(
                f"n={n:>7}, order={order:<7}, "
                f"median={median_ms:.6f} ms, "
                f"min={min_ms:.6f} ms, "
                f"max={max_ms:.6f} ms, "
                f"sum={result:.17g}"
            )

print(f"\nRaw timing measurements saved to {csv_path}")