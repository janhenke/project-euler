#include <cstdlib>
#include <print>

#include <generators.hpp>

///
/// Solver for Project Euler problem number 007
///
/// https://projecteuler.net/problem=007
///
int main() {
    auto result = 0ULL;
    auto count = 0uz;

    for (auto gen = project_euler::common::prime_numbers_u64(); const auto value : gen)
    {
        if (count == 10'001)
        {
            result = value;
            break;
        }
        ++count;
    }

    std::println("Project Euler problem 007");
    std::println("");
    std::println("Solution: {}", result);
    return EXIT_SUCCESS;
}