//
// Created by Jan Henke on 06.04.25.
//

#ifndef NUMERIC_PROPERTIES_HPP
#define NUMERIC_PROPERTIES_HPP

#include <cstdint>
#include <concepts>
#include <vector>

namespace project_euler::common
{
    template<std::unsigned_integral T>
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
}

#endif //NUMERIC_PROPERTIES_HPP
