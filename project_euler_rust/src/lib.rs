///
///
/// # Arguments
///
/// * `n`:
///
/// returns: Vec<u64, Global>
///
/// # Examples
///
/// ```
///
/// ```
pub fn fibonacci_below(n: u64) -> Vec<u64> {
    let mut a: u64 = 0;
    let mut b: u64 = 1;
    let mut result: Vec<u64> = Vec::new();
    while b < n {
        result.push(b);
        let temp = a + b;
        a = b;
        b = temp;
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn fibonacci_below_test() {
        let result = fibonacci_below(10);
        assert_eq!(result, vec![1, 1, 2, 3, 5, 8])
    }
}
