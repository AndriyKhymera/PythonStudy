import sys

"""
def sum(num1, num2):
    print(num1 + num2)

func()
sum(1, 2)
 
sys.stdout.write("hi\n")

for i in range(1, 11):
	print(i)


def whileFunc(limit):
	loop(limit)	

def loop(limit):
	var = 1
	while var < limit:
		inc_num(var)
		print_number(var)

def inc_num(num):
	num = num +1
	
def print_number(var):
    print(var)
whileFunc(11)
"""

def printByLines(*lines):
	print len(lines)
	for index in range(0, len(lines)):
		print("size: " + str(len(lines[index])) + ", xline: " +lines[index] + "\n")

	for line in lines:
		print(str(line))

printByLines("1", "2", "3")



