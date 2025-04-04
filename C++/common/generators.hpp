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
    auto fibonacci_generator(std::function<bool(T)>) -> coro::generator<const T>;

    template <std::unsigned_integral T>
    auto integer_factorisation(T) -> coro::generator<const T>;
}

#endif //GENERATORS_HPP
