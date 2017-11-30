def main():
    while con != "n":
        value = raw_input("Enter a value")
        con = raw_input("One more?(y/n):") != "n"

def read_value():
    string_1 = input("hi, give me input")
    print(string_1)

def loop_input():
    con = "y"
    file = open("userInput.txt", "r+")
    print (file.read())

    while con != "n":
        value = raw_input("Enter a value: ")
        file.write(value)
        con = raw_input("One more?(y/n):")
    file.close()

def print_all(locals_dict):
    for key, value in locals_dict.items():
        print key, value

loop_input()
