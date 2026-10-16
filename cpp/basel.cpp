#include <cmath>
#include <iomanip>
#include <iostream>

double basel_sum(int n) {
    double total = 0.0;

    for (int k = 1; k <= n; ++k) {
        const double x = static_cast<double>(k);
        const double term = 1.0 / (x * x);
        total += term;
    }

    return total;
}

int main() {
    const double reference = std::acos(-1.0) * std::acos(-1.0) / 6.0;
    const int test_values[] = {1, 2, 3, 1000, 10000};

    std::cout << std::scientific << std::setprecision(10);

    for (int n : test_values) {
        const double result = basel_sum(n);
        const double absolute_difference = std::abs(reference - result);
        const double relative_difference =
            absolute_difference / std::abs(reference) * 100.0;

        std::cout << "n = " << n << '\n';
        std::cout << "  Sum:      " << std::setprecision(17)
                  << result << '\n';
        std::cout << std::setprecision(10);
        std::cout << "  Abs diff: " << absolute_difference << '\n';
        std::cout << "  Rel diff: " << relative_difference << "%\n\n";
    }

    return 0;
}
