def opener(filename, delimiter=None):
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.strip().split(delimiter)
            lines.append(line)

    if len(lines) == 1:
        for v in line:
            return v
    else:
        return lines
