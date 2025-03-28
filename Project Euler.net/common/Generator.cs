using System.Numerics;

namespace common;

public static class Generator
{
    public static IEnumerable<T> Fibonacci<T>()
        where T : IUnsignedNumber<T>, INumber<T>, IMinMaxValue<T>, IComparable<T>
    {
        return Fibonacci<T>(_ => true);
    }

    public static IEnumerable<T> Fibonacci<T>(Func<T, bool> predicate)
        where T : IUnsignedNumber<T>, INumber<T>, IMinMaxValue<T>, IComparable<T>
    {
        var a = T.Zero;
        var b = T.One;

        while (predicate(b) && (T.MaxValue - b) > a)
        {
            yield return b;
            var tmp = a + b;
            a = b;
            b = tmp;
        }
    }

    public static IEnumerable<T> IntegerFactorisation<T>(T value) where T : IUnsignedNumber<T>, INumber<T>
    {
        var remainder = value;
        var divisor = T.One + T.One;
        while (remainder > T.One)
        {
            if (remainder % divisor == T.Zero)
            {
                remainder /= divisor;
                yield return divisor;
            }
            else
            {
                divisor += T.One;
            }
        }
    }
}