
import math
import time


def find_stagnation(limit: int = 200_000_000) -> None:
    total = 0.0
    reference = math.pi**2 / 6.0
    start = time.perf_counter()

    for k in range(1, limit + 1):
        x = float(k)
        term = 1.0 / (x * x)
        updated = total + term

        if updated == total:
            elapsed = time.perf_counter() - start
            absolute_difference = abs(reference - total)
            relative_difference = (
                absolute_difference / abs(reference) * 100.0
            )

            print("Status: stagnation detected")
            print(f"First attempted index: {k}")
            print(f"Last successful addition: {k - 1}")
            print(f"Stored sum: {total:.17g}")
            print(f"Absolute difference: {absolute_difference:.10e}")
            print(f"Relative difference: {relative_difference:.10e}%")
            print(f"Elapsed time: {elapsed:.6f} seconds")
            return

        total = updated

    elapsed = time.perf_counter() - start
    print(f"Status: limit reached ({limit})")
    print(f"Last completed index: {limit}")
    print(f"Stored sum: {total:.17g}")
    print(f"Elapsed time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    find_stagnation()
