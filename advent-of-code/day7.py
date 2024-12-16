import node_stack
import operator
allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

TEST = ["+","*"]


def day7():
    totalsum=0
    with open("day7_little.txt") as file:
        for line in file:
            line = line.strip().split()
            value = line[0]
            value = int(value[:len(value)-1])
            check = line[0:]
            
            if tester(line):
                print("correct!")
                print(line)
                totalsum += value
            else:
                print("false")
            

def ops_choices(ops):
    choices = []
    while choices[len(ops)-1]:...
def tester(line):
    value = line[0]
    value = int(value[:len(value)-1])
    line = line[1:]
    line= list(map(int,line))
    ops = [0 for i in line[1:]]
    ops_choice= ops_choices(ops)




day7()