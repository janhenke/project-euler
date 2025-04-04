fn main() {
    let mut sum: u64 = 0;

    for i in 1..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i;
        }
    }

    println!("Project Euler problem 001");
    println!();
    println!("Solution: {}", sum);
}
