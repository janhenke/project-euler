using System.Numerics;

namespace common;

public class NumberTraits
{
    public static bool IsPalindrome<T>(T value) where T : IUnsignedNumber<T>, INumber<T>
    {
        var digits = new List<T>();
        var remainder = value;
        var ten = T.CreateChecked(10);

        while (remainder > T.Zero)
        {
            digits.Add(remainder % ten);
            remainder = remainder / ten;
        }

        var count = digits.Count;
        for (var i = 0; i < count / 2; i++)
        {
            if (digits[i] != digits[count - i - 1])
            {
                return false;
            }
        }

        return true;
    }
}