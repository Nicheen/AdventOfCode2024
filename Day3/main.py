import re

def process_file(file_path):
    reg_exp = r"([^\s(]+)\s*\(([^)]+)\)"
    total = 0

    with open(file_path, 'r') as file:
        for row in file:
            matches = re.findall(reg_exp, row)
            for match in matches:
                func_name, args = match
                if func_name == "mul" and "," in args:
                    try:
                        arg1, arg2 = map(int, map(str.strip, args.split(",")))
                        if 1 <= len(str(arg1)) <= 3 and 1 <= len(str(arg2)) <= 3:
                            total += arg1 * arg2
                            print(f"{func_name}({args})")
                    except ValueError:
                        # Handle cases where arguments are not integers
                        continue
    return total

if __name__ == "__main__":
    input_file = "./Day3/input.txt"
    result = process_file(input_file)
    print(f"Total: {result}")
