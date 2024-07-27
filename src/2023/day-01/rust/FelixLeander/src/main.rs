use itertools::Itertools;

const INPUT: &str = include_str!("input");
fn main() {
    day_one_puzzle_one();
    day_one_puzzle_two();
}

fn day_one_puzzle_two() {
    const NUM_TEXT: &[&str] = &[
        "0", "zero", "1", "one", "2", "two", "3", "three", "4", "four", "5", "five", "6", "six", "7",
        "seven", "8", "eight", "9", "nine",
    ];

    let lines = INPUT.lines();
    let map = lines.map(|line| {
        let (x , z) = NUM_TEXT.iter()
            .enumerate()
            .flat_map(|(i, n)|
            {
                line.match_indices(n)
                    .map(move |(idx, _)|
                    {
                        (idx, i / 2)
                    })
            })
            .minmax()
            .into_option()
            .unwrap();

        return x.1 * 10 + z.1;
    });

    let sum: usize = map.sum();
    println!("RESULT; Day-1-b: {}", sum);
}

fn day_one_puzzle_one() {
    let lines = INPUT.lines();

    let mut result = 0;
    let predicate = |c: char| c.is_digit(10);

    for line in lines {
        let pos_first = line.find(predicate);
        let pos_second = line.rfind(predicate);

        if pos_first.is_none() || pos_second.is_none()  {
            continue;
        }

        let index_first = pos_first.unwrap();
        let index_second = pos_second.unwrap();

        let char_a = line.chars().nth(index_first).expect("FUCK A:");
        let char_b = line.chars().nth(index_second).expect("FUCK B:");

        let mut set = String::from("");
        set.push(char_a);
        set.push(char_b);

        let value: i32 = set.parse().expect("YEEEEET");

        result += value;
    }

    println!("RESULT; Day-1-a: {}" , result);
}

/*
fn day_one_puzzle_two_three() {
    const NUM_TEXT :[(&str, &str); 10] = [
        ("0","zero"),
        ("1","one"),
        ("2","two"),
        ("3","three"),
        ("4","four"),
        ("5","five"),
        ("6","six"),
        ("7","seven"),
        ("8","eight"),
        ("9","nine")
    ];

    let char_is_num = |c: char| c.is_digit(10);

    let text_lines = include_str!("input.text").lines().enumerate().map(|(size, data)| (size, data));
    let mut sum = 0;

    for line in text_lines {
        println!("{}", "");
        println!("{}", "");

        let mut finished_line = String::from(line.1);
        println!("{}", finished_line);

        for nt in NUM_TEXT {
            let result = finished_line.replacen(nt.1, nt.0, 1);
            println!("o: {}", finished_line);
            println!("n: {}", result);
            finished_line = result;
        }
        println!("{}", finished_line);

        let pos_first = finished_line.find(char_is_num);
        let pos_last = finished_line.rfind(char_is_num);
        if pos_first.is_none() || pos_last.is_none() {
            println!("Invalid x: {}", finished_line);
            return;
        }

        let char_a = finished_line.chars().nth(pos_first.unwrap());
        let char_b = finished_line.chars().nth(pos_last.unwrap());
        if char_a.is_none() || char_b.is_none() {
            println!("Invalid y: {}", finished_line);
            return;
        }
        println!("{}, {}", char_b.unwrap(), char_b.unwrap());

        let mut num_text = String::from("");
        num_text.push(char_a.unwrap());
        num_text.push(char_b.unwrap());

        let may_num: Result<u32, <u32 as FromStr>::Err> = num_text.parse();
        if may_num.is_err() {
            println!("Invalid z: {}", num_text);
            return;
        }

        let num  = may_num.unwrap();
        println!("{}", num);
        sum += num;
    }
    println!("RESULT: {}", sum);
}
*/
