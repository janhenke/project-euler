//
// Created by Jan Henke on 19.03.25.
//
#include "fibonacci.hpp"

auto fibonacci::fibonacci_below(const std::uint64_t n) -> std::vector<std::uint64_t>
{
    std::uint64_t a = 0, b = 1;
    std::vector<std::uint64_t> result;
    result.reserve(n);

    while (b < n)
    {
        result.push_back(b);
        const auto tmp = a + b;
        a = b;
        b = tmp;
    }
    return result;
}
