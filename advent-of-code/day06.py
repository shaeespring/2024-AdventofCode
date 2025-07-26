def arrayer(location=None):
    lines = []
    with open("inputfile.txt") as file:

        for line in file:
            line = line.strip()
            lines.append(line)

        array = []

        for line in lines:
            # iterate over the characters in the line
            inner = []
            for char in line:
                inner.append(char)
            array.append(inner)
        if location != None:
            array[location[0]][location[1]] = "#"
        return array


def find_guard(array):
    for y in range(len(array)):
        for x in range(len(array[0])):

            if array[x][y] == "^":
                return (x, y)


def find_items(array):
    items = []
    for y in range(len(array)):
        for x in range(len(array[0])):

            if array[x][y] == "#":
                items.append((x, y))
    return items


def turn(dir):
    if dir == "^":
        return ">"
    if dir == ">":
        return "v"
    if dir == "v":
        return "<"
    if dir == "<":
        return "^"


def check(guard_pos, items):
    for item in items:
        if guard_pos == item:
            return True
    return False


def check_edges(guard_pos, array):
    if guard_pos[0] == len(array):
        return True

    if guard_pos[0] == -1:
        return True
    if guard_pos[1] == len(array[0]):
        return True
    if guard_pos[1] == -1:
        return True
    else:
        return False


def set_builder():
    s = set()
    array = arrayer()
    pos_guard = find_guard(array)
    original = pos_guard
    pos_items = find_items(array)
    dir = array[pos_guard[0]][pos_guard[1]]

    while True:
        if pos_guard != original:
            s.add(pos_guard)
        if dir == "^":
            try_guard_pos = (pos_guard[0] - 1, pos_guard[1])
        elif dir == "v":
            try_guard_pos = (pos_guard[0] + 1, pos_guard[1])
        elif dir == "<":
            try_guard_pos = (pos_guard[0], pos_guard[1] - 1)
        else:
            try_guard_pos = (pos_guard[0], pos_guard[1] + 1)

        if check(try_guard_pos, pos_items):
            dir = turn(dir)
        else:
            pos_guard = try_guard_pos
        if check_edges(try_guard_pos, array):
            # s.add(try_guard_pos)
            break
    return s, array


def test_location(location, pos_guard):
    s = dict()
    array = arrayer(location)
    org_pos = pos_guard
    pos_items = find_items(array)
    dir = array[pos_guard[0]][pos_guard[1]]

    while True:

        if pos_guard not in s:
            s[pos_guard] = 1
        else:
            s[pos_guard] += 1

            if s[pos_guard] > 4:
                return True

        if dir == "^":
            try_guard_pos = (pos_guard[0] - 1, pos_guard[1])
        elif dir == "v":
            try_guard_pos = (pos_guard[0] + 1, pos_guard[1])
        elif dir == "<":
            try_guard_pos = (pos_guard[0], pos_guard[1] - 1)
        else:
            try_guard_pos = (pos_guard[0], pos_guard[1] + 1)

        if check(try_guard_pos, pos_items):
            dir = turn(dir)

        else:
            pos_guard = try_guard_pos
        if check_edges(try_guard_pos, array):
            # s.add(try_guard_pos)
            return False


def main():
    count = 0
    seta, array = set_builder()
    pos_guard = find_guard(array)
    for location in seta:
        temporary = location
        if test_location(location, pos_guard):
            print(location)
            count += 1
    print(count)


main()
