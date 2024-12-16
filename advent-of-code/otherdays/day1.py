def lister(list1, list2):
    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        distance = list1[i] - list2[i]
        if distance < 0:
            distance = distance * -1
        sum += distance
    return sum

def similar(list1,list2):
    sim = 0  
    for x in range(len(list1)): 
        for i in range(len(list2)):
            if list1[x] == list2[i]:
                sim += list1[x]  
                break  
    return sim
        


def create_lists(filename):
    with open(filename) as file:
        list1 = list()
        list2 = list()
        for line in file:
            line = line.strip()
            line = line.split()

            for i in range(len(line)):
                if i % 2 != 0:
                    list1.append(int(line[i]))
                else:
                    list2.append(int(line[i]))
        return list1, list2


def main():
    list1, list2 = create_lists("input.txt")
    #print(lister(list1, list2))
    print(similar(list1,list2))


main()
