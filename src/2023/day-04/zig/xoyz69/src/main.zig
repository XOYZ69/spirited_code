const std = @import("std");

const filepath = "../../input.txt";

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

    while (reader.streamUntilDelimiter(writer, '\n', null)) {
        defer line.clearRetainingCapacity();
        line_index += 1;

        const cache_line = get_entry(1, line.items, ": ");
        const numbers_win = std.mem.split(u8, get_entry(0, cache_line, " | "), " ");
        // const numbers_own = std.mem.split(u8, get_entry(1, cache_line, " | "), " ");

        // std.debug.print("Win: {s} | Own: {s}\n", .{numbers_win, numbers_own});
        std.debug.print("Win: ", .{});
        for (numbers_win, 0..) |nw, i| {
            std.debug.print("{d}:{s} ", .{i, nw});
        }
        // while (numbers_win.next()) |current| {
        //     std.debug.print("{s} ", .{current});
        // }

        // std.debug.print("| Own: ", .{});
        // while (numbers_own.next()) |current| {
        //     std.debug.print("{s} ", .{current});
        // }

    } else |err| switch (err) {
        error.EndOfStream => {},
        else => return err,
    }
}