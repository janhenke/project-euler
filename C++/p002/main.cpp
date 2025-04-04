#include <cstdlib>
#include <print>

#include <generators.hpp>

///
/// Solver for Project Euler problem number 002
///
/// https://projecteuler.net/problem=002
///
int main()
{
    auto fibonacci_numbers = project_euler::common::fibonacci_generator<std::uint64_t>(
        [](const auto value) { return value < 4'000'000ULL; });

    auto result = 0ULL;

    for (const auto fibonacci_number : fibonacci_numbers)
    {
        if (fibonacci_number % 2 == 0)
        {
            result += fibonacci_number;
        }
    }

    std::println("Project Euler problem 002");
    std::println("");
    std::println("Solution: {}", result);
    return EXIT_SUCCESS;
}
