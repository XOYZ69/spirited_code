const std = @import("std");

const filepath = "../../input.txt";

const Game = struct {
    id: u8,
    red: u8,
    green: u8,
    blue: u8,

    pub fn init(id: u8, red: u8, green: u8, blue: u8) Game {
        return Game{
            .id = id,
            .red = red,
            .green = green,
            .blue = blue,
        };
    }

    pub fn test_round(self: Game, red: u8, green: u8, blue: u8) bool {
        if (red > self.red) {
            return false;
        }

        if (green > self.green) {
            return false;
        }

        if (blue > self.blue) {
            return false;
        }

        return true;
    }

    pub fn load_values(self: Game, game_line: []u8) bool {
        const game_content: []const u8 = get_entry(1, game_line, ": ");

        std.debug.print("{d}: {s}\n", .{ self.id, game_content });

        var game_sets = std.mem.split(u8, game_content, "; ");

        var return_result: bool = true;

        while (game_sets.next()) |current| {
            std.debug.print(" => {s}\n", .{current});

            var game_colors = std.mem.split(u8, current, ", ");

            var r: u8 = 0;
            var g: u8 = 0;
            var b: u8 = 0;

            while (game_colors.next()) |current_color| {
                const amount: u8 = @intCast(std.fmt.parseInt(u8, get_entry(0, current_color, " "), 10) catch {
                    std.debug.print("Failed to parse integer.\n", .{});
                    return false;
                });
                const color = get_entry(1, current_color, " ");
                std.debug.print("# Got {d} of {s}\n", .{ amount, color });

                if (std.mem.eql(u8, color, "red")) {
                    r = amount;
                }
                if (std.mem.eql(u8, color, "green")) {
                    g = amount;
                }
                if (std.mem.eql(u8, color, "blue")) {
                    b = amount;
                }
            }

            if (!self.test_round(r, g, b)) {
                return_result = false;
            }
        }

        return return_result;
    }
};

/// Returns entry at specified index.
/// Returns first if the specified index is out of range
fn get_entry(index: u8, source: []const u8, split: []const u8) []const u8 {
    var cache_line = std.mem.split(u8, source, split);

    var i: usize = 0;

    while (cache_line.next()) |current| {
        if (i == index) {
            return current;
        }
        i += 1;
    }
    return cache_line.first();
}

pub fn main() !void {
    part_one();
}

pub fn part_one() !void {
    // prepare the memory allocation
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    // open the file
    const file = try std.fs.cwd().openFile(filepath, .{});
    defer file.close();

    // wrap the file in a buffered reader
    var buf_reader = std.io.bufferedReader(file.reader());
    const reader = buf_reader.reader();

    var line = std.ArrayList(u8).init(allocator);
    defer line.deinit();

    const writer = line.writer();

    var line_index: u8 = 0;

    var sum: usize = 0;

    while (reader.streamUntilDelimiter(writer, '\n', null)) {
        defer line.clearRetainingCapacity();
        line_index += 1;

        std.debug.print("Game nr {d} => ", .{line_index});
        var newGame = Game.init(line_index, 12, 13, 14);
        if (newGame.load_values(line.items)) {
            sum += line_index;
        }

        // var cache_line = std.mem.split(u8, line.items, ":");

    } else |err| switch (err) {
        error.EndOfStream => {},
        else => return err,
    }

    std.debug.print("Result is {d}", .{sum});
}
