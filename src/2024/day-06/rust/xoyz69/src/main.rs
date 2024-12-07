use std::{collections::HashMap, fs::read_to_string};

fn read_lines(filename: &str) -> Vec<String> {
    return read_to_string(filename)
        .unwrap() // panic on possible file-reading errors
        .lines() // split the string into an iterator of string slices
        .map(String::from) // make each slice into a string
        .collect(); // gather them together into a vector
}

#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct CoordChar {
    x: i32,
    y: i32,
    c: char,
}

fn part_1(lines: &Vec<String>) {
    let mut visit_spots: HashMap<(i32, i32), CoordChar> = HashMap::new();
    let mut total_moves = 0;
    let mut guard_position: CoordChar = CoordChar {
        x: -1,
        y: -1,
        c: ' ',
    };
    let map = build_map(lines);
    let max_x = lines.iter().map(|line| line.len()).max().unwrap_or(0);
    let max_y = lines.len();

    // Iterate over the map and get the initial guard position
    for (outer_index, outer_vec) in map.iter().enumerate() {
        for (inner_index, inner_obj) in outer_vec.iter().enumerate() {
            if inner_obj.c == '^' {
                guard_position = CoordChar {
                    x: inner_index as i32,
                    y: outer_index as i32,
                    c: inner_obj.c,
                };
                break;
            }
        }
    }

    let mut guard_rotation = 0;

    println!(
        "Initial Guard position is at => x:{} / y:{} with rotation: {}",
        guard_position.x, guard_position.y, guard_rotation
    );

    visit_spots.insert((guard_position.x, guard_position.y), guard_position);

    while guard_position.x > 0
        && guard_position.x < max_x as i32 - 1
        && guard_position.y > 0
        && guard_position.y < max_y as i32 - 1
    {
        let new_coord;
        match guard_rotation {
            0 => new_coord = map[guard_position.y as usize - 1][guard_position.x as usize + 0],
            1 => new_coord = map[guard_position.y as usize + 0][guard_position.x as usize + 1],
            2 => new_coord = map[guard_position.y as usize + 1][guard_position.x as usize + 0],
            3 => new_coord = map[guard_position.y as usize + 0][guard_position.x as usize - 1],
            _ => new_coord = map[guard_position.y as usize + 0][guard_position.x as usize + 0],
        }
        if new_coord.c == '#' {
            if guard_rotation >= 3 {
                guard_rotation = 0;
            } else {
                guard_rotation += 1;
            }
        } else {
            guard_position = new_coord;
            total_moves += 1;
        }
        visit_spots.insert((guard_position.x, guard_position.y), guard_position);
    }

    println!(
        "Final Guard position is at => x:{} / y:{} with rotation: {} with {} unique fields visited after {} moves.",
        guard_position.x, guard_position.y, guard_rotation, visit_spots.len(), total_moves
    )
}

fn part_2(lines: &Vec<String>) {
    println!("--------> Part 2");
    let mut guard_position: CoordChar = CoordChar {
        x: -1,
        y: -1,
        c: ' ',
    };
    let mut init_guard_position: CoordChar = CoordChar {
        x: -1,
        y: -1,
        c: ' ',
    };
    let map = build_map(lines);
    let mut mut_map = map.clone();
    let max_x = lines.iter().map(|line| line.len()).max().unwrap_or(0);
    let max_y = lines.len();

    // Iterate over the map and get the initial guard position
    for (outer_index, outer_vec) in map.iter().enumerate() {
        for (inner_index, inner_obj) in outer_vec.iter().enumerate() {
            if inner_obj.c == '^' {
                init_guard_position = CoordChar {
                    x: inner_index as i32,
                    y: outer_index as i32,
                    c: inner_obj.c,
                };
                break;
            }
        }
    }

    let max_tries = 12_500;
    let mut total_possibilites = 0;

    println!(
        "Initial Guard position is at => x:{} / y:{} with rotation: 0",
        init_guard_position.x, init_guard_position.y
    );
    let mut run = 0;
    // Iterate over the map and get the initial guard position
    for (outer_index, outer_vec) in map.iter().enumerate() {
        for (inner_index, inner_obj) in outer_vec.iter().enumerate() {
            run += 1;
            let mut visit_spots: HashMap<(i32, i32), CoordChar> = HashMap::new();
            let mut visit_repeat: HashMap<(CoordChar, i32), CoordChar> = HashMap::new();
            let mut total_moves = 0;
            let mut guard_rotation = 0;
            guard_position = init_guard_position;
            visit_spots.insert((guard_position.x, guard_position.y), guard_position);

            if mut_map[outer_index][inner_index].c != '.' {
                println!("---> Skip");
                continue;
            }

            mut_map[outer_index][inner_index].c = '#';
            println!("\t\tNew border at: [{} / {}]", outer_index, inner_index);

            while guard_position.x > 0
                && guard_position.x < max_x as i32 - 1
                && guard_position.y > 0
                && guard_position.y < max_y as i32 - 1
            {
                let new_coord;
                match guard_rotation {
                    0 => {
                        new_coord =
                            mut_map[guard_position.y as usize - 1][guard_position.x as usize + 0]
                    }
                    1 => {
                        new_coord =
                            mut_map[guard_position.y as usize + 0][guard_position.x as usize + 1]
                    }
                    2 => {
                        new_coord =
                            mut_map[guard_position.y as usize + 1][guard_position.x as usize + 0]
                    }
                    3 => {
                        new_coord =
                            mut_map[guard_position.y as usize + 0][guard_position.x as usize - 1]
                    }
                    _ => {
                        new_coord =
                            mut_map[guard_position.y as usize + 0][guard_position.x as usize + 0]
                    }
                }
                if new_coord.c == '#' {
                    if guard_rotation >= 3 {
                        guard_rotation = 0;
                    } else {
                        guard_rotation += 1;
                    }
                } else {
                    guard_position = new_coord;
                    total_moves += 1;
                }
                visit_spots.insert((guard_position.x, guard_position.y), guard_position);

                if let Some(_) = visit_repeat.get(&(guard_position, guard_rotation)) {
                    println!("Loop");
                    continue;
                } else {
                    println!(
                        "\t--> Inserted: [{} / {} @ {}] => Character: {}",
                        guard_position.x,
                        guard_position.y,
                        guard_rotation,
                        mut_map[guard_position.y as usize][guard_position.x as usize].c
                    );
                    visit_repeat.insert((guard_position, guard_rotation), guard_position);
                }

                mut_map[outer_index][inner_index].c = '.';
            }

            total_possibilites += 1;

            println!("Run {:3}: Final Guard position is at => x:{} / y:{} with rotation: {} with {:5} unique fields visited after {:5} moves.", run, guard_position.x, guard_position.y, guard_rotation, visit_spots.len(), total_moves);
        }
    }
    println!("--------------------------");
    println!("Total Possibilites: {}", total_possibilites);
}

fn build_map(lines: &Vec<String>) -> Vec<Vec<CoordChar>> {
    let mut map: Vec<Vec<CoordChar>> = vec![];

    // Determine the maximum dimensions
    let max_x = lines.iter().map(|line| line.len()).max().unwrap_or(0);
    let max_y = lines.len();

    map.resize(max_y, vec![CoordChar { x: 0, y: 0, c: ' ' }; max_x]);
    for (y, line) in lines.iter().enumerate() {
        for (x, c) in line.chars().enumerate() {
            map[y][x] = CoordChar {
                x: x as i32,
                y: y as i32,
                c: c as char,
            };
        }
    }
    return map;
}

fn main() {
    let lines: Vec<String> = read_lines("../../.input2");

    part_1(&lines);
    part_2(&lines);
}
