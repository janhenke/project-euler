//
// Created by Jan Henke on 23.03.25.
//

#include "generators.hpp"
#include "numeric_properties.hpp"

#include <limits>
#include <utility>

template <std::unsigned_integral T>
auto project_euler::common::fibonacci_generator(const std::function<bool(T)>& predicate) -> coro::generator<const T>
{
    const T max = std::numeric_limits<T>::max();
    T a = 0;
    T b = 1;

    while (predicate(b) && max - b >= a)
    {
        co_yield b;
        a = std::exchange(b, a + b);
    }
}

template auto project_euler::common::fibonacci_generator(
    const std::function<bool(std::uint32_t)>&) -> coro::generator<const std::uint32_t>;
template auto project_euler::common::fibonacci_generator(
    const std::function<bool(std::uint64_t)>&) -> coro::generator<const std::uint64_t>;

template <std::unsigned_integral T>
auto project_euler::common::integer_factorisation(const T value) -> coro::generator<const T>
{
    T remainder = value;
    T divisor = 2;
    while (remainder > 1)
    {
        if (remainder % divisor == 0)
        {
            remainder /= divisor;
            co_yield divisor;
        }
        else
        {
            ++divisor;
        }
    }
}

template auto project_euler::common::integer_factorisation(std::uint32_t) -> coro::generator<const std::uint32_t>;
template auto project_euler::common::integer_factorisation(std::uint64_t) -> coro::generator<const std::uint64_t>;

template <std::unsigned_integral T>
auto project_euler::common::prime_numbers() -> coro::generator<const T>
{
    const T max = std::numeric_limits<T>::max();
    T i = 2;
    while (i < max)
    {
        if (common::is_prime(i))
        {
            co_yield i;
        }
        ++i;
    }
}

template auto project_euler::common::prime_numbers() -> coro::generator<const std::uint32_t>;
template auto project_euler::common::prime_numbers() -> coro::generator<const std::uint64_t>;
