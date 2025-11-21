package dev.janhenke.project_euler;

import java.math.BigDecimal;

/**
 * Base class for all Project Euler problems.
 *
 * @author Jan Henke (Jan.Henke@taujhe.de)
 */
public abstract class ProjectEulerProblemBase
{
	/// @return the problem statement to be solved.
	public String getProblemStatement()
	{
		return this.getClass().getSimpleName();
	}

	/// @return the solution to the stated mathematical problem.
	///
	/// @see #getProblemStatement
	public abstract BigDecimal solve();
}
