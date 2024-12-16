import re

def counter(filename):
    mullist = []  # List to store mul() matches
    in_dont_block = False  # Flag to track if inside a don't() block

    # Define the regular expression pattern for mul({number, number})
    pattern = r"mul\(\d+,\d+\)"

    with open(filename) as file:
        for line in file:
            # Split the string into parts using don't() and do() as delimiters
            parts = re.split(r"(don't\(\)|do\(\))", line)

            # Process each part
            for part in parts:
                if "don't()" in part:
                    # Set the flag when a don't() is found
                    in_dont_block = True
                elif "do()" in part:
                    # Reset the flag when a do() is found
                    in_dont_block = False
                elif not in_dont_block:
                    # Collect mul() values only when not inside a don't() block
                    mullist.extend(re.findall(pattern, part))

        return mullist


def multiplier(mullist):
    mult_sum = 0
    for item in mullist:
        # Remove the 'mul(' and ')' from the string to get just the numbers
        item = item[4:-1]  # Removes 'mul(' from start and ')' from end
        item1, item2 = map(int, item.split(','))  # Convert the two numbers to integers
        print(item1, item2)  # Print the pair of numbers
        mult_sum += item1 * item2  # Multiply and accumulate the sum

    return mult_sum


def main():
    mullist = counter("day3.txt")  # Get all mul() matches from the file
    print("Multiplications List:", mullist)
    
    mult_sum = multiplier(mullist)  # Calculate the sum of all multiplications
    print("Total sum:", mult_sum)


main()
