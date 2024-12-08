# Part 1 & Part 2
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

def check_values_part_1(values) -> bool:
    previous_value = 0
    level_counter = 0
    for i, value in enumerate(values):
        if i > 0:
            if previous_value + 3 >= value >= previous_value + 1:
                level_counter += 1
            elif previous_value - 3 <= value <= previous_value - 1:
                level_counter -= 1
            else:
                print(f"{values}: Unsafe because of {previous_value} and {value} ==> {abs(previous_value - value)}")
                return False

            if level_counter not in [i, -i]:
                print(f"{values}: Sometime is wrong here: {level_counter}, {i}, {-i}")
                return False

            if i == len(values) - 1: 
                return True

        previous_value = value

def check_values_part_2(values, index=-1, printable=False) -> int:
    previous_value = 0
    level_counter = 0

    if printable:
        a = values.copy()
        print(f"{a} without {a.pop(index)}", end="\t")

    if index != -1: 
        del values[index]
    
    for i, value in enumerate(values):
        if i > 0:
            if previous_value + 3 >= value >= previous_value + 1:
                level_counter += 1
            elif previous_value - 3 <= value <= previous_value - 1:
                level_counter -= 1
            else:
                if printable: 
                    print("UNSAFE")
                return i

            if level_counter not in [i, -i]:
                if printable: 
                    print("UNSAFE")
                return i

            if i == len(values) - 1:
                if printable: 
                    print("SAFE")
                return -1

        previous_value = value
if __name__ == "__main__":
    PART1 = False
    PART2 = not PART1
    file = open("./Day2/input.txt",'r')
    content = file.read()
    list_of_content = content.split('\n')

    if PART1:
        counter = 0
        for row in list_of_content:
            values = [int(nr) for nr in row.split(" ")]
            counter += check_values_part_1(values)
        print(counter)

    if PART2:
        counter = 0
        for row in list_of_content:
            values = [int(nr) for nr in row.split(" ")]
            returned_value = check_values_part_2(values)
            if returned_value >= 0:
                new_returned_value = check_values_part_2(values, returned_value, True)
                if new_returned_value == -1:
                    counter += 1
            elif returned_value == -1:
                counter += 1
        print("\n", counter)



