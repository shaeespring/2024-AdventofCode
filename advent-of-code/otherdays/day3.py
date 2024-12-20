import re

def counter(filename):
    mullist = []  # to store mul() matches
    in_dont_block = False  # if inside a don't() block

    # pattern for mul({number, number})
    pattern = r"mul\(\d+,\d+\)"

    with open(filename) as file:
        for line in file:
            # split the string into parts 
            parts = re.split(r"(don't\(\)|do\(\))", line)

            for part in parts:
                if "don't()" in part:
                    
                    in_dont_block = True
                elif "do()" in part:
                    in_dont_block = False
                elif not in_dont_block:
                    # collect mul() values only when not inside a don't() block
                    mullist.extend(re.findall(pattern, part))

        return mullist


def multiplier(mullist):
    mult_sum = 0
    for item in mullist:
        item = item[4:-1]  # removes 'mul(' from start and ')' from end
        item1, item2 = map(int, item.split(','))  
        print(item1, item2)  # print the pair of numbers
        mult_sum += item1 * item2  

    return mult_sum


def main():
    mullist = counter("day3.txt")  
    print(mullist)
    
    mult_sum = multiplier(mullist)  
    print(mult_sum)


main()
