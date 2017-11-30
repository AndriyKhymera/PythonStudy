number = 8
mask = 0b10
test = number | mask

print(number)
print(mask)
print(bin(test))
print(bin(test ^ 0b1111))
