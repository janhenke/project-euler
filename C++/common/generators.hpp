//
// Created by Jan Henke on 23.03.25.
//

#ifndef GENERATORS_HPP
#define GENERATORS_HPP

#include <coro/generator.hpp>
#include <functional>

namespace project_euler::common
{
    template <std::unsigned_integral T>
    auto fibonacci_generator() -> coro::generator<T>
    {
        return fibonacci_generator<T>([](auto) { return true; });
    }

    template <std::unsigned_integral T>
    auto fibonacci_generator(const std::function<bool(T)>&) -> coro::generator<const T>;

    template <std::unsigned_integral T>
    auto integer_factorisation(T) -> coro::generator<const T>;
    extern template auto integer_factorisation<std::uint32_t>(std::uint32_t) -> coro::generator<const std::uint32_t>;
    extern template auto integer_factorisation<std::uint64_t>(std::uint64_t) -> coro::generator<const std::uint64_t>;

    /**
     * Produces a generator of prime numbers.
     *
     * @tparam T Return type
     * @return A generator of prime numbers
     */
    template <std::unsigned_integral T>
    auto prime_numbers() -> coro::generator<const T>;
    extern template auto prime_numbers<std::uint32_t>() -> coro::generator<const std::uint32_t>;
    extern template auto prime_numbers<std::uint64_t>() -> coro::generator<const std::uint64_t>;
    using prime_numbers_u32 = decltype(prime_numbers<std::uint32_t>());
    using prime_numbers_u64 = decltype(prime_numbers<std::uint64_t>());
}

#endif //GENERATORS_HPP
