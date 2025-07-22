import operator

allowed_operators = {
    "+": operator.add,
    "*": operator.mul,
}


def day7():
    totalsum = 0
    with open("day7_little.txt") as file:
        for line in file:
            line = line.strip().split()
            value = line[0]
            value = int(value[: len(value) - 1])
            check = line[1:]

            if tester(check, value):
                print("correct!")
                print(line)
                totalsum += value
                # eventually this will add the test values

            else:
                ...
        print(totalsum)


def ops_choices(line, value, ind, current_val):
    if ind == len(line):
        return current_val == value

    else:

        val =  str(current_val)+str(line[ind])

        if ops_choices(line, value, ind + 1, int(val)):
            return True

        val = line[ind] + current_val
        if ops_choices(line, value, ind + 1, val):
            return True

        val = line[ind] * current_val
        if ops_choices(line, value, ind + 1, int(val)):
            return True


def tester(line, value):
    sum = 0
    line = list(map(int, line))
    if ops_choices(line, value, 1,line[0]):
        return True


day7()
