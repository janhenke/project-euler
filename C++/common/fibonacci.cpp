//
// Created by Jan Henke on 19.03.25.
//
#include "fibonacci.hpp"

template <std::integral T>
auto fibonacci::fibonacci_below(const T n) -> std::vector<T>
{
    T a = 0, b = 1;
    std::vector<T> result;
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

template auto fibonacci::fibonacci_below(std::uint16_t n) -> std::vector<std::uint16_t>;
template auto fibonacci::fibonacci_below(std::uint32_t n) -> std::vector<std::uint32_t>;
template auto fibonacci::fibonacci_below(std::uint64_t n) -> std::vector<std::uint64_t>;
