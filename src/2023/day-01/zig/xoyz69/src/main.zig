const std = @import("std");
const print = std.debug.print;

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

        for (line.items, 0..) | item, index | {

            if(item < '0' or item > '9') {
                // print(" => Skip non-integer: {u}\n", .{ item });
                continue;
            }

            const cache = try std.fmt.parseInt(i8, &[1]u8{ item }, 10);

            if(cache != 0) {
                print("i: {d} => {d}\n", .{ index, cache });

                if(cur[0] == 0) {
                    cur[0] = @intCast(cache);
                } else {
                    cur[1] = @intCast(cache);
                }
            }
        }

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
