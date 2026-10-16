#include <cmath>
#include <iomanip>
#include <iostream>

int main() {
    const double S_b = 1.644934057834575;
    const double pi = std::acos(-1.0);
    const double S_ref = (pi * pi) / 6.0;

    const double D_abs = std::abs(S_b - S_ref);
    const double D_percent = 100.0 * D_abs / std::abs(S_ref);

    std::cout << std::setprecision(17);
    std::cout << "Language: C++\n";
    std::cout << "S_b:       " << S_b << '\n';
    std::cout << "S_ref:     " << S_ref << '\n';
    std::cout << std::scientific << std::setprecision(12);
    std::cout << "D_abs:     " << D_abs << '\n';
    std::cout << "D_percent: " << D_percent << "%\n";
}
