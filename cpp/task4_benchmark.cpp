#include <algorithm>
#include <chrono>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <cmath>

using Clock = std::chrono::steady_clock;

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
    const int sizes[] = {1000, 10000, 100000, 1000000};
    const int warmups = 5;
    const int repeats = 10;

    std::ofstream csv("results/timing_cpp.csv");
    csv << "language,order,n,run,batch_size,per_call_ms,returned_sum\n";
    csv << std::setprecision(17);

    std::cout << "TASK 4: C++ BENCHMARK\n";
    std::cout << "Warm-ups: " << warmups
              << ", timed runs: " << repeats << "\n\n";

    for (int n : sizes) {
        for (int order = 0; order < 2; ++order) {
            const bool reverse = (order == 1);
            const std::string order_name =
                reverse ? "reverse" : "forward";

            for (int i = 0; i < warmups; ++i) {
                volatile double result = calculate_sum(n, reverse);
                (void)result;
            }

            std::vector<double> times;
            double result = 0.0;

            for (int run = 1; run <= repeats; ++run) {
                const auto start = Clock::now();
                result = calculate_sum(n, reverse);
                const auto end = Clock::now();

                const double elapsed_ms =
                    std::chrono::duration<double, std::milli>(
                        end - start).count();

                times.push_back(elapsed_ms);

                csv << "C++," << order_name << "," << n << ","
                    << run << ",1," << elapsed_ms << ","
                    << result << "\n";
            }

            std::sort(times.begin(), times.end());

            const double median_ms =
                (times[4] + times[5]) / 2.0;
            const double min_ms = times.front();
            const double max_ms = times.back();

            std::cout << std::fixed << std::setprecision(6)
                      << "n=" << n
                      << ", order=" << order_name
                      << ", median=" << median_ms << " ms"
                      << ", min=" << min_ms << " ms"
                      << ", max=" << max_ms << " ms"
                      << ", sum=" << std::setprecision(17)
                      << result << "\n";
        }
    }

    std::cout << "\nRaw timing measurements saved to "
                 "results/timing_cpp.csv\n";
    return 0;
}