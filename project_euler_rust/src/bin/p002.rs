use project_euler_rust::fibonacci_below;

fn main() {
    let fibonacci_numbers = fibonacci_below(4_000_000);
    let mut result: u64 = 0;

    for number in fibonacci_numbers {
        if number % 2 == 0 {
            result += number;
        }
    }

    println!("Project Euler problem ###");
    println!();
    println!("Solution: {}", result);
}
