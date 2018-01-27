extern crate rand;

use std::io;
use std::io::Write;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("🔍  숫자를 맞춰봐!");
    
    let secret = rand::thread_rng().gen_range(1, 101);
    
    println!("👄  비밀 숫자를 말해줘");

    loop {
        print!("❯❯❯ ");
        io::stdout().flush()
            .expect("❌  실패!");
        let mut guess = String::new();

        io::stdin().read_line(&mut guess)
            .expect("❌  실패!");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("❌  숫자를 입력해줘야지");
                continue;
            },
        };

        match guess.cmp(&secret) {
            Ordering::Less => println!("⚠️  너무 작은걸"),
            Ordering::Greater => println!("⚠️  너무 큰걸"),
            Ordering::Equal => {
                println!("✅  정답이야!");
                break;
            }
        }
    }
}
