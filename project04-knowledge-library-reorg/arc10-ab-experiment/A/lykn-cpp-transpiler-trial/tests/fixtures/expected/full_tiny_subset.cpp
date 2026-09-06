#include <iostream>

int main() {
    int a{20};
    int b{(a + 2)};
    int c{(b - 5)};
    int d{(c * (8 / 4))};
    std::cout << (d + 1) << "\n";
    std::cout << ((b * c) / 3) << "\n";
    return 0;
}
