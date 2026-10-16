#include <cmath>
#include <iomanip>
#include <iostream>

const int N_VALUES[] = {1000, 10000, 100000, 1000000};

double calculate_sum(int n, bool reverse) {
    double total = 0.0;

    if (reverse) {
        for (int k = n; k >= 1; --k) {
            double x = static_cast<double>(k);
            total += 1.0 / (x * x);
        }
    } else {
        for (int k = 1; k <= n; ++k) {
            double x = static_cast<double>(k);
            total += 1.0 / (x * x);
        }
    }

    return total;
}

int main() {
    const double pi = std::acos(-1.0);
    const double S_ref = (pi * pi) / 6.0;

    std::cout << std::setprecision(17);
    std::cout << "TASK 3: FORWARD AND REVERSE SUMMATION\n";
    std::cout << "Reference value: " << S_ref << '\n';

    for (int n : N_VALUES) {
        for (int order = 0; order < 2; ++order) {
            bool reverse = (order == 1);
            double result = calculate_sum(n, reverse);

            double d_abs = std::abs(S_ref - result);
            double d_percent = 100.0 * d_abs / std::abs(S_ref);

            std::cout << std::scientific << std::setprecision(12);
            std::cout << "n=" << n
                      << ", order=" << (reverse ? "reverse" : "forward")
                      << ", sum=" << std::setprecision(17) << result
                      << ", D_abs=" << std::scientific
                      << std::setprecision(12) << d_abs
                      << ", D_percent=" << d_percent << "%"
                      << ", tail=(" << 1.0 / (n + 1)
                      << ", " << 1.0 / n << ")\n";
        }
    }

    std::cout << "\nSmall-case verification:\n";
    const double expected[] = {1.0, 1.25, 49.0 / 36.0};

    for (int n = 1; n <= 3; ++n) {
        double actual = calculate_sum(n, false);
        bool passed = std::abs(actual - expected[n - 1]) < 1e-14;

        std::cout << "n=" << n
                  << ", computed=" << std::setprecision(17) << actual
                  << ", expected=" << expected[n - 1]
                  << ", passed=" << (passed ? "true" : "false")
                  << '\n';
    }

    return 0;
}