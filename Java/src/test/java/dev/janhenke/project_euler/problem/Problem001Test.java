package dev.janhenke.project_euler.problem;

import org.junit.jupiter.api.Test;

import java.math.BigDecimal;

import static org.assertj.core.api.Assertions.assertThat;

/// Unit test for [Problem001].
///
/// @author Jan Henke (Jan.Henke@taujhe.de)
class Problem001Test
{
	@Test
	void solve()
	{
		final var solver = new Problem001();
		assertThat(solver.solve()).isEqualTo(BigDecimal.valueOf(233168L));
	}
}
