//
// Created by Jan Henke on 19.03.25.
//

#ifndef FIBONACCI_HPP
#define FIBONACCI_HPP

#include <cstdint>
#include <vector>

#include "project_euler_common_export.h"

namespace fibonacci
{
    /**
     *
     * @param n Limit for the greatest fibonacci number
     * @return The list of fibonacci numbers so that none is greater than n
     */
     PROJECT_EULER_COMMON_EXPORT auto fibonacci_below(std::uint64_t n) -> std::vector<std::uint64_t>;
}

#endif //FIBONACCI_HPP
