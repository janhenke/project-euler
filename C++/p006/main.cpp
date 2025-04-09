#include <cstdlib>
#include <print>

///
/// Solver for Project Euler problem number 006
///
/// https://projecteuler.net/problem=006
///
int main()
{
    auto result = 0ULL;
    auto squares = 0ULL;

    for (auto i = 1ULL; i <= 100; ++i)
    {
        result += i;
        squares += i * i;
    }

    result *= result;
    result -= squares;

    std::println("Project Euler problem 006");
    std::println("");
    std::println("Solution: {}", result);
    return EXIT_SUCCESS;
}
