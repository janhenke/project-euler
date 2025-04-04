using common;

var result = 1UL;
var factors = new Dictionary<uint, int>();

for (var i = 2U; i <= 20; i++)
{
    var tmp = Generator.IntegerFactorisation(i).ToList();
    for (var j = 0U; j <= 20; j++)
    {
        if (tmp.Contains(j))
        {
            if (factors.TryGetValue(j, out var value))
            {
                factors[j] = Math.Max(tmp.Count(num => num == j), value);
            }
            else
            {
                factors[j] = tmp.Count(num => num == j);
            }
        }
    }

    foreach (var (key, value) in factors)
    {
        result *= (uint) Math.Pow(key, value);
    }
}


Console.WriteLine("Project Euler problem ###");
Console.WriteLine("");
Console.WriteLine("Solution: {0}", result);