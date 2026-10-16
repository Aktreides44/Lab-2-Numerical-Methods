import csv
import os
import matplotlib.pyplot as plt

os.makedirs("plots", exist_ok=True)
os.makedirs("results", exist_ok=True)

S_REF = 1.6449340668482264
SIZES = [1000, 10000, 100000, 1000000]
LANGUAGES = ["Python", "C++", "Julia"]
ORDERS = ["forward", "reverse"]

# Verified numerical results from Task 3.
# Values are recorded separately for each language and order.
numerical_results = {
    "Python": {
        "forward": [
            (1000, 1.6439345666815615),
            (10000, 1.6448340718480652),
            (100000, 1.6449240668982423),
            (1000000, 1.6449330668487701),
        ],
        "reverse": [
            (1000, 1.6439345666815597),
            (10000, 1.6448340718480596),
            (100000, 1.6449240668982263),
            (1000000, 1.6449330668487263),
        ],
    },
    "C++": {
        "forward": [
            (1000, 1.64393456668156146),
            (10000, 1.64483407184806518),
            (100000, 1.64492406689824233),
            (1000000, 1.64493306684877005),
        ],
        "reverse": [
            (1000, 1.64393456668155968),
            (10000, 1.64483407184805963),
            (100000, 1.64492406689822634),
            (1000000, 1.64493306684872631),
        ],
    },
    "Julia": {
        "forward": [
            (1000, 1.6439345666815615),
            (10000, 1.6448340718480652),
            (100000, 1.6449240668982423),
            (1000000, 1.6449330668487701),
        ],
        "reverse": [
            (1000, 1.6439345666815597),
            (10000, 1.6448340718480596),
            (100000, 1.6449240668982263),
            (1000000, 1.6449330668487263),
        ],
    },
}

# Write a numerical-results CSV.
with open("results/numerical_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "language", "order", "n", "computed_sum",
        "absolute_difference", "relative_difference_percent",
        "tail_lower_bound", "tail_upper_bound"
    ])

    for language, orders in numerical_results.items():
        for order, values in orders.items():
            for n, result in values:
                d_abs = abs(S_REF - result)
                d_percent = 100 * d_abs / abs(S_REF)

                writer.writerow([
                    language, order, n, repr(result),
                    f"{d_abs:.12e}", f"{d_percent:.12e}",
                    f"{1/(n+1):.12e}", f"{1/n:.12e}"
                ])

# Plot 1: absolute difference against n.
plt.figure()
for language in LANGUAGES:
    for order in ORDERS:
        data = numerical_results[language][order]
        ns = [item[0] for item in data]
        errors = [abs(S_REF - item[1]) for item in data]
        plt.loglog(ns, errors, marker="o",
                   label=f"{language} {order}")

plt.loglog(SIZES, [1/n for n in SIZES],
           linestyle="--", label="1/n reference")
plt.xlabel("Number of terms (n)")
plt.ylabel("Absolute difference")
plt.title("Absolute Difference vs Number of Terms")
plt.grid(True, which="both")
plt.legend(fontsize="small")
plt.tight_layout()
plt.savefig("plots/task5_absolute_difference.png", dpi=200)

# Load measured timing data.
timing_files = {
    "Python": "results/timing_python.csv",
    "C++": "results/timing_cpp.csv",
    "Julia": "results/timing_julia.csv",
}

timings = {}
for language, path in timing_files.items():
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (language, row["order"], int(row["n"]))
            timings.setdefault(key, []).append(float(row["per_call_ms"]))

# Plot 2: Difference between forward and reverse sums.
plt.figure()

for language in LANGUAGES:
    forward = dict(numerical_results[language]["forward"])
    reverse = dict(numerical_results[language]["reverse"])

    ns = SIZES
    order_differences = [
        abs(forward[n] - reverse[n]) for n in ns
    ]

    plt.loglog(
        ns,
        order_differences,
        marker="o",
        label=language
    )

plt.xlabel("Number of terms (n)")
plt.ylabel("Absolute difference between orders")
plt.title("Forward vs Reverse Summation Difference")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("plots/task5_order_difference.png", dpi=200)


# Plot 3: median execution time against n.
plt.figure()
for language in LANGUAGES:
    for order in ORDERS:
        ns = []
        medians = []

        for n in SIZES:
            values = timings[(language, order, n)]
            ns.append(n)
            medians.append(sorted(values)[len(values)//2]
                           if len(values) % 2
                           else (sorted(values)[len(values)//2 - 1]
                                 + sorted(values)[len(values)//2]) / 2)

        plt.loglog(ns, medians, marker="o",
                   label=f"{language} {order}")

plt.xlabel("Number of terms (n)")
plt.ylabel("Median execution time (ms)")
plt.title("Median Execution Time vs Number of Terms")
plt.grid(True, which="both")
plt.legend(fontsize="small")
plt.tight_layout()
plt.savefig("plots/task5_median_time.png", dpi=200)

print("Task 5 files generated:")
print("  results/numerical_results.csv")
print("  plots/task5_absolute_difference.png")
print("  plots/task5_median_time.png")