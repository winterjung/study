use std::io;

fn main() {
    println!("숫자를 맞춰보세요!");
    let mut guess = String::new();

    io::stdin().read_line(&mut guess)
        .expect("실패!");

    println!("너의 입력은: {}", guess);
}
