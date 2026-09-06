#include <iostream>

int main() {
    const int base{8};
    const int doubled{(base * 2)};
    const int adjusted{(doubled - 5)};
    std::cout << (adjusted / 3) << "\n";
    return 0;
}
