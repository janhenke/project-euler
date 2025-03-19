#include <cstdlib>
#include <print>

///
/// Solver for Project Euler problem number 001
///
/// https://projecteuler.net/problem=1
///
int main()
{
    unsigned long long sum = 0;
    for (unsigned long long i = 1; i < 1000; ++i)
    {
        if (i % 3 == 0 || i % 5 == 0)
        {
            sum += i;
        }
    }

    std::println("Project Euler problem 001");
    std::println("==========================");
    std::println("Solution: {}", sum);
    return EXIT_SUCCESS;
}
