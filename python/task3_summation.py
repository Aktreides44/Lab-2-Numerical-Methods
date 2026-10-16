import math

S_ref = math.pi**2 / 6.0
N_VALUES = [10**3, 10**4, 10**5, 10**6]


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


print("TASK 3: FORWARD AND REVERSE SUMMATION")
print(f"Reference value: {S_ref:.17g}")

for n in N_VALUES:
    for order in ["forward", "reverse"]:
        result = calculate_sum(n, reverse=(order == "reverse"))

        d_abs = abs(S_ref - result)
        d_percent = 100.0 * d_abs / abs(S_ref)
        tail_lower = 1.0 / (n + 1)
        tail_upper = 1.0 / n

        print(
            f"n={n:>7}, order={order:<7}, "
            f"sum={result:.17g}, "
            f"D_abs={d_abs:.12e}, "
            f"D_percent={d_percent:.12e}%, "
            f"tail=({tail_lower:.12e}, {tail_upper:.12e})"
        )