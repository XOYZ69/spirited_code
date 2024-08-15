const std = @import("std");

const filepath = "../../input.txt";
const invalid_symbols = ".0123456789";

const Coord = struct {
    x: i32,

    pub fn hash(self: Coord) u64 {
        var cache_hash = std.hash.hash(i32, self.x);
        cache_hash = std.hash.hash(i32, self.y, hash);
        return cache_hash;
    }
};

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

    var cache_parent_array = std.ArrayList(std.ArrayList(usize)).init(allocator);

    while (reader.streamUntilDelimiter(writer, '\n', null)) {
        var object_position = std.ArrayList(usize).init(allocator);
        defer line.clearRetainingCapacity();

        std.debug.print("{d} -> ", .{line_index});
        for (line.items[0 .. line.items.len - 2], 0..) |item, i| {
            if (!is_valid_character(item)) {
                continue;
            }
            try object_position.append(i);
            std.debug.print("[{d}: {c}]", .{ i, item });
        }

        try cache_parent_array.append(object_position);
        std.debug.print("\n", .{});

        line_index += 1;
    } else |err| switch (err) {
        error.EndOfStream => {},
        else => return err,
    }

    while (line_index > 0) {
        line_index -= 1;

        const current_list_opt = cache_parent_array.items[line_index];

        std.debug.print("{d}: ", .{line_index});

        for (current_list_opt.items) |item| {
            std.debug.print("{d} ", .{item});
        }

        current_list_opt.deinit();
        std.debug.print("\n", .{});
    }

    cache_parent_array.deinit();
}
