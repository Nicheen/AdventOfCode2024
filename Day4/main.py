test_input = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"

word = "XMAS"
number = 0

for row in test_input.split("\n"):
    string_list = list(row)
    for i, letter in enumerate(row):
        if "XMAS" in string_list:
            
    new_string = "".join(string_list)
    print(new_string)