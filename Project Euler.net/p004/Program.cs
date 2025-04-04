using common;

var result = 0;

for (var i = 999; i >= 0; i--)
{
    for (var j = 999; j >= 0; j--)
    {
        var tmp = i * j;
        if (NumberTraits.IsPalindrome((uint)tmp) && tmp > result)
        {
            result = tmp;
        }
    }
}

Console.WriteLine("Project Euler problem 004");
Console.WriteLine("");
Console.WriteLine("Solution: {0}", result);