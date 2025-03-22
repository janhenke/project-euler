//
// Created by Jan Henke on 19.03.25.
//

#ifndef FIBONACCI_HPP
#define FIBONACCI_HPP

#include <concepts>
#include <vector>

#include "project_euler_common_export.h"

namespace fibonacci
{
    /**
     *
     * @tparam T Integral type
     * @param n Limit for the greatest fibonacci number
     * @return The list of fibonacci numbers so that none is greater than n
     */
    template <std::integral T>
    PROJECT_EULER_COMMON_EXPORT auto fibonacci_below(T n) -> std::vector<T>;
}

#endif //FIBONACCI_HPP
