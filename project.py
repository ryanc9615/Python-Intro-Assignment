first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

# First calculations

print(first_num + second_num)
print(first_num - second_num)
print(first_num * second_num)
if second_num == 0: 
    print("Denominator is zero")
else:
    print(first_num/second_num)

if first_num > second_num:
    print(f"{first_num} is greater than {second_num}")
else: 
    print(f"{second_num} is greater than {first_num}")
