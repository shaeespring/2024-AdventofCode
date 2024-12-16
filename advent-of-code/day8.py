class Arrayer():
    __slots__ = ["__array"]
    def __init__(self):
        lines = []
        with open("day8_little.txt") as file:

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

        self.__array = array
    def is_on_board(self,pos):

        if pos[0] >=0 and pos[1] >= 0:
            try:
                pos = self.__array[pos[0]][pos[1]]
                return True
            except IndexError:
                return False
        else:
            return False
    def __len__(self):
        count = 0
        for line in self.__array:
            count += 1
        return count

def diction_cr(array):
    diction = dict()
    for line_num in range(len(array)):
        for chr_in in range(len(array[line_num])):
            if array[line_num][chr_in] != ".":
                if array[line_num][chr_in] not in diction:
                    diction[array[line_num][chr_in]] = [(line_num,chr_in)]
                else:
                    diction[array[line_num][chr_in]] += [(line_num,chr_in)]
                
    return diction

def main():
        
    # for line in arrayer():
    #     print(line)
    array = Arrayer()

    diction_cr(array)
main()

