
#include <chrono>
#include <cmath>
#include <iomanip>
#include <iostream>

int main() {
    constexpr long long limit = 200'000'000;

    double total = 0.0;
    const double pi = std::acos(-1.0);
    const double reference = pi * pi / 6.0;

    const auto start = std::chrono::steady_clock::now();

    for (long long k = 1; k <= limit; ++k) {
        const double x = static_cast<double>(k);
        const double term = 1.0 / (x * x);
        const double updated = total + term;

        if (updated == total) {
            const auto end = std::chrono::steady_clock::now();
            const double elapsed =
                std::chrono::duration<double>(end - start).count();

            const double abs_diff = std::abs(reference - total);
            const double rel_diff = abs_diff / std::abs(reference) * 100.0;

            std::cout << std::setprecision(17);
            std::cout << "Status: stagnation detected\n";
            std::cout << "First attempted index: " << k << '\n';
            std::cout << "Last successful addition: " << k - 1 << '\n';
            std::cout << "Stored sum: " << total << '\n';

            std::cout << std::scientific << std::setprecision(10);
            std::cout << "Absolute difference: " << abs_diff << '\n';
            std::cout << "Relative difference: " << rel_diff << "%\n";
            std::cout << "Elapsed time: " << elapsed << " seconds\n";

            return 0;
        }

        total = updated;
    }

    std::cout << "Status: limit reached (" << limit << ")\n";
    std::cout << std::setprecision(17);
    std::cout << "Stored sum: " << total << '\n';

    return 0;
}
