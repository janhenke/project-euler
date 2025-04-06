#include <cstdlib>
#include <print>

#include "numeric_properties.hpp"

///
/// Solver for Project Euler problem number 004
///
/// https://projecteuler.net/problem=004
///
int main()
{
    auto result = 0ULL;

    for (auto i = 999ULL; i > 0; --i)
    {
        for (auto j = 999ULL; j > 0; --j)
        {
            if (const auto product = i * j; project_euler::common::is_palindrome(product) && product > result)
            {
                result = product;
            }
        }
    }

    std::println("Project Euler problem 004");
    std::println("");
    std::println("Solution: {}", result);
    return EXIT_SUCCESS;
}
