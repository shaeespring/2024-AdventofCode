def day5():
    totalsum = 0
    with open("inputfile.txt") as file:
        rules = []
        for line in file:
            line = line.strip()
            if len(line) == 5:
                line = line.split("|")
                rule = (line[0],line[1])
                rules.append(rule)
            else:
                line = line.split(",")
                for rule in rules:
                    try:
                        if line.index(rule[0])<line.index(rule[1]):
                            continue
                    except ValueError:
                        continue
                    else:
                        sortish(rules,line)
                        totalsum += int(line[len(line)//2])
                        
    return totalsum

def sortish(rules, line):
    
        for rule in rules:
            try:
                if not line.index(rule[0])<line.index(rule[1]):
                    temp = line.index(rule[0])
                    line.pop(temp)
                    line.insert(line.index(rule[1]),rule[0])
                    sortish(rules,line)
                
                elif line.index(rule[0])<line.index(rule[1]): 
                    if rules.index(rule) == len(rules)-1:
                        return line
                else:
                    break
            except ValueError:
                    continue
                


print(day5())




# def orderer():
#     diction = dict()
#     order = list()
#     total_sum = 0
#     with open("day5.txt") as file:
#         for line in file:
#             line = line.strip()
#             if len(line) == 5:
#                 line = line.split("|")
#                 first = int(line[0])
#                 second = int(line[1])
#                 if first not in diction:
#                     diction.update({first: list()})
#                     order.append(first)

#                 diction[first].append(second)
#                 if second not in diction:
#                     diction.update({second: list()})
#                     order.append(second)

#             elif len(line) == 0:
#                 order = sortish(order, diction)

#                 print(order)
#                 print(diction[order[0]])
#             else:
#                 line = line.split(",")

                
#                 for i in range(len(line)):
                    
#                         if i >= 1:
#                             try:
#                                 index_before = order.index(int(line[i - 1]))
#                                 index_now = order.index(int(line[i]))
#                             except ValueError:
#                                 continue
#                             if index_now < index_before:
#                                 print("nah")
#                                 break
#                             else:
#                                 if i == len(line)-1:
                                        
#                                     print("yippee: ", line)
#                                     total_sum += int(line[len(line) // 2])  # Middle element of the list
#                                 else: 
#                                     continue

#     return total_sum

# def lessthan(dic, value, order):
#     for index in range(len(dic[value])):
#         if index_find(order, value) < index_find(order, dic[value][index]):
#             continue
#         else:
#             return False
#     return True


# def index_find(a_list, val):
#     for i in range(len(a_list)):
#         if a_list[i] == val:
#             return i
#     return None  # Returns len if not found


# print(orderer())
