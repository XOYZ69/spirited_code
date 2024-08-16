const std = @import("std");

const filepath = "../../input.txt";
const invalid_symbols = ".0123456789";
const numerics = "0123456789";

fn is_numeric(char: u8) bool {
    for (numerics) |num| {
        if (num == char) {
            return true;
        }
    }
    return false;
}

fn is_valid_character(char: u8) bool {
    if (char == '\n') {
        return false;
    }

    for (invalid_symbols) |symbol| {
        if (symbol == char) {
            return false;
        }
    }
    return true;
}

fn get_int_length(num: usize) usize {
    var length: usize = 1;

    while (std.math.pow(usize, 10, length) < num) {
        length += 1;
    }
    return length - 1;
}

fn symbol_is_edging(pos_num: usize, value: usize, line_to_check: []std.ArrayListAligned(usize, null), line_index: usize) bool {
    var found_symbol = false;
    const value_length = get_int_length(value);

    if (pos_num <= 0) {
        return false;
    }

    if (line_index > 0) {
        if (line_index > line_to_check.len - 1) {
            return false;
        }
    }

    for (line_to_check[line_index].items) |symbol| {
        if (symbol >= pos_num - 1) {
            if (symbol <= pos_num + value_length + 1) {
                found_symbol = true;
            }
        }
    }

    return found_symbol;
}

pub fn main() !void {
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

    var line_symbol_index = std.ArrayList(std.ArrayList(usize)).init(allocator);
    var line_number_map = std.ArrayList(std.AutoHashMap(usize, i32)).init(allocator);

    while (reader.streamUntilDelimiter(writer, '\n', null)) {
        var object_position = std.ArrayList(usize).init(allocator);
        var number_position = std.AutoHashMap(usize, i32).init(allocator);
        defer line.clearRetainingCapacity();

        std.debug.print("{d} -> ", .{line_index});
        var num_len: usize = 0;
        var last_character_numeric = false;
        var curent_character_numeric = false;
        for (line.items[0 .. line.items.len - 2], 0..) |item, i| {
            curent_character_numeric = is_numeric(item);

            if (curent_character_numeric) {
                num_len += 1;
            } else if (last_character_numeric) {
                const cache_string: []u8 = line.items[i - num_len .. i];
                std.debug.print("({d}: {s}) ", .{ i - num_len, cache_string });
                const cache = try std.fmt.parseInt(i32, cache_string, 10);
                try number_position.put(i - num_len, cache);
                num_len = 0;
            }

            last_character_numeric = curent_character_numeric;

            if (!is_valid_character(item)) {
                continue;
            }
            try object_position.append(i);
            std.debug.print("[{d}: {c}]", .{ i, item });
        }

        try line_symbol_index.append(object_position);
        try line_number_map.append(number_position);
        std.debug.print("\n", .{});

        line_index += 1;
    } else |err| switch (err) {
        error.EndOfStream => {},
        else => return err,
    }

    var total_sum: i32 = 0;

    while (line_index > 0) {
        line_index -= 1;

        const current_line_symbols = line_symbol_index.items[line_index];
        var current_line_numbers = line_number_map.items[line_index];

        std.debug.print("{d}: ", .{line_index});

        for (current_line_symbols.items) |item| {
            std.debug.print("{d} ", .{item});
        }

        std.debug.print("\n -> ", .{});

        var number_iterator = current_line_numbers.keyIterator();
        while (number_iterator.next()) |entry| {
            const key = entry.*;
            const value = current_line_numbers.get(key) orelse -1;
            std.debug.print("([", .{});
            var is_edged = false;

            if (line_index > 0) {
                if (symbol_is_edging(key, @intCast(value), line_symbol_index.items, line_index - 1)) {
                    std.debug.print("x", .{});
                    is_edged = true;
                } else {
                    std.debug.print("-", .{});
                }
            }

            if (symbol_is_edging(key, @intCast(value), line_symbol_index.items, line_index)) {
                std.debug.print("x", .{});
                is_edged = true;
            } else {
                std.debug.print("-", .{});
            }

            if (line_index < line_symbol_index.items.len - 1) {
                if (symbol_is_edging(key, @intCast(value), line_symbol_index.items, line_index + 1)) {
                    std.debug.print("x", .{});
                    is_edged = true;
                } else {
                    std.debug.print("-", .{});
                }
            }

            if (is_edged) {
                total_sum += value;
            }

            std.debug.print("] | {d}: {d}) ", .{ key, value });
        }

        std.debug.print("\n", .{});
        current_line_numbers.deinit();
    }

    for (line_symbol_index.items) |item| {
        item.deinit();
    }

    line_symbol_index.deinit();
    line_number_map.deinit();

    std.debug.print("Result: {d}", .{total_sum});
}
