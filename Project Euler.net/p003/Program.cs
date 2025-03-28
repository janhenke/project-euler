using common;

var result = 0UL;

foreach (var prime in Generator.IntegerFactorisation(600851475143UL))
{
    if (prime > result)
    {
        result = prime;
    }
}

Console.WriteLine("Project Euler problem 003");
Console.WriteLine("");
Console.WriteLine("Solution: {0}", result);