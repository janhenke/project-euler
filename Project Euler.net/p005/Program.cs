using common;

var result = 1UL;
var factors = new Dictionary<uint, int>();

for (var i = 2U; i <= 20; i++)
{
    var candidates = new Dictionary<uint, int>();
    foreach (var value in Generator.IntegerFactorisation(i))
    {
        candidates.TryGetValue(value, out var count);
        candidates[value] = count + 1;
    }

    foreach (var (key, value) in candidates)
    {
        factors.TryGetValue(key, out var factor);
        factors[key] = factor < value ? value : factor;
    }
}

foreach (var factor in factors)
{
    for (var j = 0; j < factor.Value; j++)
    {
        result *= factor.Key;
    }
}


Console.WriteLine("Project Euler problem 005");
Console.WriteLine("");
Console.WriteLine("Solution: {0}", result);