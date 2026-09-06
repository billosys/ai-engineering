#include <iostream>

int main() {
    const int x{1};
    const int y{(x + 2)};
    std::cout << (y * 3) << "\n";
    return 0;
}
