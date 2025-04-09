#include <cstdlib>
#include <map>
#include <print>

#include "generators.hpp"

///
/// Solver for Project Euler problem number 005
///
/// https://projecteuler.net/problem=005
///
int main()
{
    auto result = 1ULL;

    auto factors = std::map<unsigned long long, std::size_t>();

    for (auto i = 2ULL; i < 20ULL; ++i)
    {
        auto candidate = std::map<unsigned long long, std::size_t>();
        for (auto value : project_euler::common::integer_factorisation(i))
        {
            candidate[value]++;
        }
        for (const auto& [factor, count] : candidate)
        {
            if (factors[factor] < count)
            {
                factors[factor] = count;
            }
        }
    }

    for (const auto& [factor, count] : factors)
    {
        for (auto i = 0uz; i < count; ++i)
        {
            result *= factor;
        }
    }

    std::println("Project Euler problem 005");
    std::println("");
    std::println("Solution: {}", result);
    return EXIT_SUCCESS;
}
