import os

# Part 1 of the advent of code
file = open("./day1_input.txt",'r')
content = file.read()

split_list = [i.split("   ") for i in content.split("\n")][0:-1]
first_list = [i[0] for i in split_list]
second_list = [i[1] for i in split_list]
first_list.sort()
second_list.sort()

diff = sum([abs(int(first_list[i]) - int(second_list[i])) for i in range(len(first_list))])

print(diff)

# Part 2 of the advent of code
answer = 0
for number in first_list:
    if number in second_list:
        n = second_list.count(number)
        answer += n * int(number)

print(answer)