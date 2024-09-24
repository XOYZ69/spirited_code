use std::ptr::null;

// use colored::Colorize;
const INPUT: &str = include_str!("../../../input");

struct Range {
    char_infos: Vec<CharInfo>,
}
struct CharInfo {
    line_index: usize,
    pos_index: u32,
    char: char,
    kind: Kind,
}

enum Kind {
    Dot,
    Number,
    Symbol,
}


impl Copy for Kind {

}

impl Clone for Kind {
    fn clone(&self) -> Self {
         match self {
            Kind::Dot => Kind::Dot,
            Kind::Number => Kind::Number,
            Kind::Symbol => Kind::Symbol,
        }
    }
}

fn main() {
    let char_infos = get_parsed();

    let ranges = parse_to_groups(char_infos);

    for range  in ranges {
        for char_info in range.char_infos {
            if char_info.pos_index == 0 {
                println!();
            }
            print!("{}", char_info.char)
        }
    }
}

fn parse_to_groups(char_infos: Vec<CharInfo>) -> Vec<Range> {
    let mut ranges: Vec<Range> = Vec::new();

    let mut last_info: Option<CharInfo> = None;
    let mut range: Range;
    for char_info in char_infos {
        if range == null
            || char_info.pos_index == 0
            || char_info.char != last_info.expect("Felix!!!!!!!!!!!!").char
        {
            range = Range {
                char_infos: Vec::new(),
            };

            let clone = CharInfo {
                line_index: char_info.line_index,
                pos_index: char_info.pos_index,
                char: char_info.char,
                kind: char_info.kind,
            };
            range.char_infos.push(clone);
        }

        last_info = Some(char_info);
    }

    ranges
}

fn get_parsed() -> Vec<CharInfo> {
    let mut infos: Vec<CharInfo> = Vec::new();
    let mut index = 0;
    for line in INPUT.lines() {
        let mut pos = 0;
        for char in line.chars() {
            let kind: Kind;
            if char == '.' {
                kind = Kind::Dot;
            } else if char.is_digit(10) {
                kind = Kind::Number;
            } else {
                kind = Kind::Symbol;
            }

            infos.push(CharInfo {
                line_index: index,
                pos_index: pos,
                char,
                kind,
            });
            pos += 1;
        }
        index += 1;
    }

    return infos;
}

//
// struct NumsPos {
//     line_index: usize,
//     index_start: u32,
//     index_end: u32,
//     value: u32,
//     valid: bool,
// }
//
// fn main2() {
//     let mut nums_pos: Vec<NumsPos> = Vec::new();
//     let mut line_index = 0;
//     for line in INPUT.lines() {
//         for result in line_to_nums(line, line_index) {
//             nums_pos.push(result);
//         }
//         line_index += 1;
//     }
//
//     validate(&mut nums_pos);
//
//     let mut snum = 0;
//     for nums_po in nums_pos {
//         snum +=nums_po.value;
//     }
//
//     println!("RESULT-X:{}", snum)
// }
// fn validate(nums_pos: &mut Vec<NumsPos>) {
//     for mut num_pos in nums_pos {
//         if below(&mut num_pos) || beside(&mut num_pos) || above(&mut num_pos) {
//             num_pos.valid = true;
//         }
//
//         if num_pos.valid {
//             println!(
//                 "RESULT:{}: {} is {}",
//                 num_pos.line_index, num_pos.value, num_pos.valid
//             )
//         }
//     }
// }
//
// fn line_to_nums(line: &str, index_line: usize) -> Vec<NumsPos> {
//     let mut start: i32 = -1;
//     let mut end: i32 = -1;
//
//     let mut nums_pos: Vec<NumsPos> = Vec::new();
//     let mut nums_text = String::new();
//     let mut i = 0;
//     while i < line.len() {
//         let current_option = line.chars().nth(i);
//         if current_option.is_none() {
//             panic!("AAAAAAAAAAAAAAAAAAA")
//         }
//
//         let current_value = current_option.unwrap();
//         if current_value.is_digit(10) {
//             nums_text.push(current_value);
//
//             if start == -1 {
//                 start = i as i32;
//             }
//         } else {
//             if start != -1 {
//                 end = (i - 1) as i32;
//             }
//
//             if nums_text.len() != 0 {
//                 let result = nums_text.parse::<u32>().expect("AAHAHAHAHAHAHAHA");
//
//                 let value = NumsPos {
//                     line_index: index_line,
//                     value: result,
//                     index_start: start as u32,
//                     index_end: end as u32,
//                     valid: false,
//                 };
//
//                 nums_pos.push(value);
//                 nums_text = String::new();
//             }
//         }
//
//         i += 1;
//     }
//
//     return nums_pos;
// }
//
// fn below(num_pos: &mut NumsPos) -> bool {
//     if (num_pos.line_index + 1) == INPUT.len() {
//         return false;
//     }
//
//     let line_below = INPUT.lines().nth(num_pos.line_index).expect("i'm sorry mom");
//
//     let min = (num_pos.index_start - 1) as usize;
//     let max = (num_pos.index_end + 1) as usize;
//     let range = &line_below[min..max];
//
//     // println!("{}", range);
//     // println!();
//
//     for character in range.chars() {
//         if character != '.' && !character.is_digit(10) {
//             num_pos.valid = true;
//             return true;
//         }
//     }
//
//     return false;
// }
//
// fn beside(num_pos: &mut NumsPos) -> bool {
//     let line = INPUT.lines().nth(num_pos.line_index).expect("i'm sorry mom");
//
//     if num_pos.index_start - 1 <= 0 {
//         let before = line.chars().nth((num_pos.index_start - 1) as usize).expect("underflow");
//         if before != '.' {
//             return true;
//         }
//     }
//
//     if num_pos.index_start + 1 > line.len() as u32 {
//         let after = line.chars().nth((num_pos.index_end + 1) as usize).expect("overflow");
//         if after != '.' {
//             return true;
//         }
//     }
//
//     return false;
// }
//
// fn above(num_pos: &mut NumsPos) -> bool {
//     if num_pos.line_index as i32 == 0 {
//         return false;
//     }
//
//     let line_above = INPUT
//         .lines()
//         .nth(num_pos.line_index as usize)
//         .expect("i'm sorry mom");
//
//     let min = (num_pos.index_start - 1) as usize;
//     let max = (num_pos.index_end + 1) as usize;
//     let range = &line_above[min..max];
//
//     // println!("{}", range);
//     // println!();
//
//     for character in range.chars() {
//         if character != '.' && !character.is_digit(10) {
//             num_pos.valid = true;
//             return true;
//         }
//     }
//
//     return false;
// }
