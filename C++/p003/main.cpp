#include <cstdlib>
#include <print>

#include <generators.hpp>

///
/// Solver for Project Euler problem number 003
///
/// https://projecteuler.net/problem=003
///
int main()
{
    auto result = 0ULL;

    for (const auto prime : project_euler::common::integer_factorisation(600851475143ULL))
    {
        if (prime > result)
        {
            result = prime;
        }
    }

    std::println("Project Euler problem 003");
    std::println("");
    std::println("Solution: {}", result);
    return EXIT_SUCCESS;
}
