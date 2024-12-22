def arrayer(filename):
    lines = []
    with open(filename) as file:

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

        return array