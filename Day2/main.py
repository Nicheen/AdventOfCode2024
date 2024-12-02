file = open("./Day2/input.txt",'r')
content = file.read()

split_list = content.split("\n")

def is_safe(previous, current, future) -> bool:
    diff_current_previous = abs(current - previous)
    diff_current_future = abs(current - future)
    return (1 <= diff_current_previous <= 3 and 1 <= diff_current_future <= 3)

def is_increasing(previous, current, future) -> bool:
    return (previous < current) and (current < future)

def check(list) -> bool:
    return all(i == list[0] for i in list)

n_safe = 0
for entry in split_list:

    entry_list = entry.split(" ")

    l = []
    s = []

    for i, number_text in enumerate(entry_list):
        
        if 0 < i < len(entry_list) - 1:

            current_number  = int(number_text)
            previous_number = int(entry_list[i - 1])
            future_number   = int(entry_list[i + 1])

            s.append(is_safe(previous_number, current_number, future_number))   
            l.append(is_increasing(previous_number, current_number, future_number))

    print(l, s)
    if check(l) and all(s):
        n_safe += 1

print(n_safe)