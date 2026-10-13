
import math


def basel_sum(n: int) -> float:
    """Calculate the first n terms of the Basel series using a scalar loop."""
    total = 0.0

    for k in range(1, n + 1):
        x = float(k)
        term = 1.0 / (x * x)
        total += term

    return total


def main():
    reference = math.pi**2 / 6.0

    for n in [1, 2, 3, 1_000, 10_000]:
        result = basel_sum(n)
        absolute_difference = abs(reference - result)
        relative_difference = (
            absolute_difference / abs(reference) * 100.0
        )

        print(f"n = {n:>6}")
        print(f"  Sum:       {result:.17g}")
        print(f"  Abs diff:  {absolute_difference:.10e}")
        print(f"  Rel diff:  {relative_difference:.10e}%")
        print()


if __name__ == "__main__":
    main()
