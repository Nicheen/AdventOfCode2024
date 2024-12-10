
if __name__ == "__main__":
    file = open("./Day5/input.txt",'r')
    content = file.read()
    list_of_content = content.split('\n\n')
    
    rules = [[int(nr) for nr in rule.split("|")] for rule in list_of_content[0].split('\n')]
    input = [[int(nr) for nr in code.split(",")] for code in list_of_content[1].split('\n')]

    sum = 0
    for code in input:
        order = code.copy()
        
        for rule in rules:
            if rule[0] in order and rule[1] in order:
                index_r0 = order.index(rule[0])
                index_r1 = order.index(rule[1])
                if index_r0 > index_r1:
                    # We swap the order of the numbers if the rule is not currently applied
                    order[index_r0], order[index_r1] = order[index_r1], order[index_r0]

        if order == code:
            # Add the middle number to the final sum
            sum += code[int(len(code) / 2)]

    print(f"Answer: %i" % sum)