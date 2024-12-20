def checker(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            line = line.strip().split()  
            
            # if the line is valid 
            if doub_checker(line):
                count += 1
                continue #skip removing each value
            
            #removing one element at a time and check if it becomes valid
            valid = False
            for i in range(len(line)):
                new_line = line[:i] + line[i+1:]  # remove the element at index i
                if doub_checker(new_line):
                    valid = True 
                    break #get out of for loop so the new line doesn't become False

            if valid:
                count += 1  # if we found a valid sequence after removing one element

        
        print(count)

def doub_checker(line):
    inc = False
    dec = False
    valid = True  # if the line is valid

    # check the differences between consecutive elements
    for num in range(1, len(line)):
        diff = int(line[num]) - int(line[num-1])

        # check if the difference is between 1 and 3 (inclusive)
        if 1 <= abs(diff) <= 3:
            if diff > 0:  # if the sequence is increasing
                if dec:  # if it was previously decreasing, it's invalid
                    valid = False
                    break
                inc = True
            elif diff < 0:  # if the sequence is decreasing
                if inc:  # if it was previously increasing, it's invalid
                    valid = False
                    break
                dec = True
        else:
            valid = False
            break  # no valid sequence if the difference is not between 1 and 3

    return valid
checker("day2.txt")