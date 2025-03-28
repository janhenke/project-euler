// See https://aka.ms/new-console-template for more information

var result = 0UL;

for (var i = 0UL; i < 1_000; i++)
{
    if (i % 3 == 0 || i % 5 == 0)
    {
        result += i;
    }
}

Console.WriteLine("Project Euler problem 001");
Console.WriteLine("");
Console.WriteLine("Solution: {0}", result);