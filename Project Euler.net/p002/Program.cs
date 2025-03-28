// See https://aka.ms/new-console-template for more information
using common;

var generator = Generator.Fibonacci<uint>(n => n < 4_000_000);

var result = 0UL;

foreach (var fibonacciNumber in generator)
{
    if (fibonacciNumber % 2 == 0)
    {
        result += fibonacciNumber;
    }
}

Console.WriteLine("Project Euler problem 002");
Console.WriteLine("");
Console.WriteLine("Solution: {0}", result);