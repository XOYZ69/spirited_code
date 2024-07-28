use std::str::Lines;

const INPUT: &str = include_str!("../../../input");

struct GameData {
    game_id: u32,
    parts: Vec<GamePart>,
}

struct GamePart {
    red: u32,
    green: u32,
    blue: u32,
}

impl GamePart {
    fn to_string(&self) -> String {
        let mut data: String = String::new();
        data.push_str("r:");
        data.push_str(self.red.to_string().as_str());

        data.push_str(" g:");
        data.push_str(self.green.to_string().as_str());

        data.push_str(" b:");
        data.push_str(self.blue.to_string().as_str());

        data.push_str("\n");
        return data;
    }
}

fn main() {
    let game_data = parse_to_game_data(INPUT.lines());
    if game_data.is_none() {
        println!("COULD NOT PARSE INPUT TO GAME DATA");
        return;
    }
    let games = game_data.unwrap();
        let result = sum_of_valid_games(&games, 12, 13, 14);
        println!("P1 Result: {}", result);

        let result = sum_of_valid_games_puzzle_part_two(&games);
        println!("P2 Result: {}", result);
}

fn parse_to_game_data(lines: Lines) -> Option<Vec<GameData>> {
    let mut games: Vec<GameData> = Vec::new();
    for line in lines {
        let colum_index = line.find(':');
        if colum_index.is_none() {
            println!("data");
            return None;
        }

        let length = "Game ".len();
        let game_id_text = &line[length..colum_index.unwrap()];
        let game_id = game_id_text.parse::<u32>();
        if game_id.is_err() {
            panic!("ERROR b: '{}'", game_id_text);
        }

        let line_parts = &line[colum_index.unwrap() + 2..];
        let game_parts = parse_to_game_parts(line_parts);
        if game_parts.is_none() {
            panic!("ERROR c: '{}'", line_parts);
        }

        let game_data = GameData {
            game_id: game_id.unwrap(),
            parts: game_parts.unwrap(),
        };
        games.push(game_data);
    }

    return Some(games);
}

fn parse_to_game_parts(text: &str) -> Option<Vec<GamePart>> {
    let mut game_parts: Vec<GamePart> = Vec::new();
    let game_parts_text = text.split("; ");
    for game_part_text in game_parts_text {
        let result = part_text_to_game_part(game_part_text);
        if result.is_none() {
            panic!("ERROR a: '{}'", game_part_text);
        }

        game_parts.push(result.unwrap());
    }

    return Some(game_parts);
}

fn part_text_to_game_part(text: &str) -> Option<GamePart> {
    let mut num_red: u32 = 0;
    let mut num_green: u32 = 0;
    let mut num_blue: u32 = 0;
    let parts = text.split(", ");
    for part in parts {
        let mut part_parts = part.split(' ');

        let part_num = part_parts.next().unwrap();
        let part_text = part_parts.next().unwrap();

        let num = part_num.parse::<u32>();
        if num.is_err() {
            panic!("ERROR x: '{}'", part_num);
        }

        if part_text.eq("red") {
            num_red = num.unwrap();
        } else if part_text.eq("green") {
            num_green = num.unwrap();
        } else if part_text.eq("blue") {
            num_blue = num.unwrap();
        } else {
            panic!("ERROR Y: NO MATCH")
        }
    }

    return Some(GamePart {
        red: num_red,
        green: num_green,
        blue: num_blue,
    });
}

fn sum_of_valid_games(game_data: &Vec<GameData>, red: u32, green: u32, blue: u32) -> u32 {
    let mut valid_game_data: Vec<&GameData> = Vec::new();

    for game in game_data {
        if game
            .parts
            .iter()
            .all(|x| x.red <= red && x.green <= green && x.blue <= blue)
        {
            valid_game_data.push(game);
        }
    }

    let result: u32 = valid_game_data.iter().map(|x| x.game_id).sum();
    return result;
}

fn sum_of_valid_games_puzzle_part_two(game_data: &Vec<GameData>) -> u32 {
    game_data.iter().map(|x| GamePart {
        red: x.parts.iter().map(|m| m.red).max().unwrap(),
        green: x.parts.iter().map(|m| m.green).max().unwrap(),
        blue: x.parts.iter().map(|m| m.blue).max().unwrap(),
    }).map(|m| m.red * m.green * m.blue).sum()
}
