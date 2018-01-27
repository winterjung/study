extern crate rand;

use std::io;
use rand::Rng;

fn main() {
    println!("숫자를 맞춰보세요!");
    
    let secret = rand::thread_rng().gen_range(1, 101);
    println!("비밀 숫자는 {}", secret);
    
    let mut guess = String::new();

    io::stdin().read_line(&mut guess)
        .expect("실패!");

    println!("너의 입력은: {}", guess);
}
