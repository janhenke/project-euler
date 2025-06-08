//
// Created by Jan Henke on 06.04.25.
//

#ifndef NUMERIC_PROPERTIES_HPP
#define NUMERIC_PROPERTIES_HPP

#include <concepts>
#include <cmath>
#include <vector>

namespace project_euler::common
{
    template <std::unsigned_integral T>
    constexpr bool is_palindrome(const T number)
    {
        auto digits = std::vector<T>();
        T remaining = number;
        while (remaining > 0)
        {
            digits.push_back(remaining % 10);
            remaining /= 10;
        }

        auto size = std::size(digits);
        for (std::size_t i = 0; i < size / 2; ++i)
        {
            if (digits[i] != digits[size - i - 1])
            {
                return false;
            }
        }
        return true;
    }

    template <std::unsigned_integral T>
    constexpr bool is_prime(const T number)
    {
        if (number == 2 || number == 3)
            return true;
        if (number < 2 || number % 2 == 0)
            return false;
        if (number < 9)
            return true;
        if (number % 3 == 0)
            return false;
        T r = static_cast<T>(std::sqrt(number));
        T f = 5;
        while (f <= r)
        {
            if (number % f == 0)
                return false;
            if (number % (f + 2) == 0)
                return false;
            f += 6;
        }
        return true;
    }
}

#endif //NUMERIC_PROPERTIES_HPP
