const std = @import("std");
const print = std.debug.print;

// False for first part
const secondPart = true;

pub fn main() !void {
    
    // prepare the memory allocator
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    // open the file
    const file = try std.fs.cwd().openFile("data/input.txt", .{});
    defer file.close();

    // wrap the file in a bufferd reader
    var buf_reader = std.io.bufferedReader(file.reader());
    const reader = buf_reader.reader();

    var line = std.ArrayList(u8).init(allocator);
    defer line.deinit();

    const writer =  line.writer();
    var line_index: usize = 0;

    var sum: usize = 0;
    var cur = [2]usize{ 0, 0 };

    while (reader.streamUntilDelimiter(writer, '\n', null)) {
        // clear the so we can reuse it
        defer line.clearRetainingCapacity();

        cur = [2]usize{0, 0};

        line_index += 1;

        print("{d} -- {s}\n", .{ line_index, line.items});

        var i: usize = 0;
        while (i < line.items.len) : (i+=1) {
            if (sliceToValue(line.items[i..])) |val| {
                if(cur[0] == 0) {
                    cur[0] = @intCast(val);
                } else {
                    cur[1] = @intCast(val);
                }
            }
        }
        
        print(" ---> Found this in the line: {d} / {d}\n", .{ cur[0], cur[1] });

        if(cur[1] == 0) {
            cur[1] = cur[0];
        }

        print("{d} += {d} * 10 + {d} = ", .{ sum, cur[0], cur[1]});
        sum += cur[0] * 10 + cur[1];
        print("{d}\n", .{sum});

    } else |err| switch (err) {
        error.EndOfStream => {
            if (line.items.len > 0) {
                line_index += 1;
                print("{d} -- {s} [Last line]\n", .{ line_index, line.items});
            }
        },
        else => return err,
    }

    print("Total lines: {d}\n", .{ line_index });
    print("Total sum: {d}", .{sum});
}

// Thanks mate: https://github.com/yanis-fourel/aoc2023-zig/blob/master/day1/2.zig
fn startsWith(str: []const u8, substr: []const u8) bool {
    var i: u32 = 0;
    while (i < substr.len) : (i += 1) {
        if (i >= str.len or str[i] != substr[i]) {
            return false;
        }
    }
    return true;
}

fn sliceToValue(str: []const u8) ?u8 {

    if (str[0] >= '0' and str[0] <= '9') {
        return str[0] - '0';
    }

    if (!secondPart) {
        return null;
    }

    const digitstr = [9][]const u8{ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

    var i: u8 = 0;
    while (i < 9) : (i += 1) {
        if (startsWith(str, digitstr[i])) {
            return i + 1;
        }
    }

    return null;
}