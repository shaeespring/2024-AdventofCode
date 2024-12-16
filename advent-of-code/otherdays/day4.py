X = "X"
M = "M"
A = "A"
S = "S"


def arrayer():
    lines = []
    with open("day4.txt") as file:

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


def count_horz(anarray):
    # count = 0
    # with open("day4.txt") as file:
    #     for line in file:
    #         line = line.strip()
    #         for i in range(len(line) - 2):

    #             if (
    #                 line[i] == X
    #                 and line[i + 1] == M
    #                 and line[i + 2] == A
    #                 and line[i + 3] == S
    #             ):
    #                 count += 1
    #             if (
    #                 line[i] == X
    #                 and line[i - 1] == M
    #                 and line[i - 2] == A
    #                 and line[i - 3] == S
    #             ):
    #                 count += 1

    # return count
    count = 0
    # print(anarray[0][0])
    # print(anarray[0][1]) # one to the right
    # print(anarray[0])

    for y in range(len(anarray)):

        for x in range(len(anarray[y])):
            
            if x<= len(anarray[y])-3 and (
                anarray[y][x] == X
                and anarray[y][x + 1] == M
                and anarray[y][x + 2] == A
                and anarray[y][x + 3] == S
            ):
                count += 1
            if x >= 3 and (
                anarray[y][x] == X
                and anarray[y][x - 1] == M
                and anarray[y][x - 2] == A
                and anarray[y][x - 3] == S
            ):
                count += 1
    return count


def count_vert(anarray):
    count = 0
    # print(anarray[0][0])
    # print(anarray[0][1]) # one to the right
    # print(anarray[0])

    for y in range(len(anarray)):

        for x in range(len(anarray[y])):
            
            if y<= len(anarray)-4 and (
                anarray[y][x] == X
                and anarray[y + 1][x] == M
                and anarray[y + 2][x] == A
                and anarray[y + 3][x] == S
            ):
                count += 1
            if y >= 3 and (
                anarray[y][x] == X
                and anarray[y - 1][x] == M
                and anarray[y - 2][x] == A
                and anarray[y - 3][x] == S
            ):
                count += 1
    return count

def part2(anarray):
    count = 0
    # print(anarray[0][0])
    # print(anarray[0][1]) # one to the right
    # print(anarray[0])

    for y in range(len(anarray)-1):

        for x in range(len(anarray[y])-1):
    
            if (
                x <= len(anarray[y]) 
                and y <= len(anarray) 
                and y >= 1
                and x >= 1):

                if (
                    anarray[y][x] == A
                    and (anarray[y + 1][x + 1] == M)
                    and (anarray[y + 1][x - 1] == S)
                    and (anarray[y - 1][x + 1] == M)
                    and (anarray[y - 1][x - 1] == S)
                ):
                    count += 1
                
                if (
                    anarray[y][x] == A
                    and (anarray[y + 1][x + 1] == S)
                    and (anarray[y + 1][x - 1] == M)
                    and (anarray[y - 1][x + 1] == S)
                    and (anarray[y - 1][x - 1] == M)
                ):
                    count += 1
                if (
                    anarray[y][x] == A
                    and (anarray[y + 1][x + 1] == M)
                    and (anarray[y + 1][x - 1] == M)
                    and (anarray[y - 1][x + 1] == S)
                    and (anarray[y - 1][x - 1] == S)
                ):
                    count += 1
                if (
                    anarray[y][x] == A
                    and (anarray[y + 1][x + 1] == S)
                    and (anarray[y + 1][x - 1] == S)
                    and (anarray[y - 1][x + 1] == M)
                    and (anarray[y - 1][x - 1] == M)
                ):
                    count += 1
    return count


def count_diag(anarray):
    count = 0
    # print(anarray[0][0])
    # print(anarray[0][1]) # one to the right
    # print(anarray[0])

    for y in range(len(anarray)):
        for x in range(len(anarray[y])) :
            
            if x<= len(anarray[y])-4 and y<= len(anarray)-4 and (
                anarray[y][x] == X
                and (anarray[y + 1][x + 1] == M )
                and (anarray[y + 2][x + 2] == A )
                and (anarray[y + 3][x + 3] == S )
            ):
                count += 1
            if (
                y >= 3
                and x >= 3
                and (
                    anarray[y][x] == X
                    and (anarray[y - 1][x - 1] == M)
                    and (anarray[y - 2][x - 2] == A)
                    and (anarray[y - 3][x - 3] == S)
                )
            ):
                count += 1
                
            if (
                
                y <=len(anarray)-4
                and x >= 3
                and (
                    anarray[y][x] == X
                    and ( anarray[y + 1][x - 1] == M)
                    and ( anarray[y + 2][x - 2] == A)
                    and ( anarray[y + 3][x - 3] == S)
                )
            ):
                count += 1
            if (
                y >= 3
                and x<= len(anarray[y])-3 
                and (
                    anarray[y][x] == X
                    and (anarray[y - 1][x + 1] == M)
                    and (anarray[y - 2][x + 2] == A)
                    and (anarray[y - 3][x + 3] == S)
                )
            ):
                count += 1

    return count


def main():
    arrayxmas = arrayer()

    # count_h = count_horz(arrayxmas)
    # count_v = count_vert(arrayxmas)
    # count_d = count_diag(arrayxmas)
    # count = count_h + count_v + count_d
    count = part2(arrayxmas)
    print(count)


main()
