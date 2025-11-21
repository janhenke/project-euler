package dev.janhenke.project_euler.problem;

import dev.janhenke.project_euler.ProjectEulerProblemBase;
import java.math.BigDecimal;

/**
 * Project Euler problem 001.
 *
 * @author Jan Henke (Jan.Henke@taujhe.de)
 */
public class Problem001 extends ProjectEulerProblemBase
{
	@Override
	public String getProblemStatement()
	{
		return """
				If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
				
				Find the sum of all the multiples of 3 or 5 below 1000.
				""";
	}

	@Override
	public BigDecimal solve()
	{
		BigDecimal result = BigDecimal.ZERO;
		for (int i = 1; i < 1000; i++)
		{
			if (i % 3 == 0 || i % 5 == 0)
			{
				result = result.add(BigDecimal.valueOf(i));
			}
		}
		return result;
	}
}
