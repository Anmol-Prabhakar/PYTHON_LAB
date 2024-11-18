def is_disarium_number(number):
    str_num = str(number)
    
     sum_of_powers = 0
      for index, digit in enumerate(str_num):
        digit = int(digit)
        power = index + 1
        sum_of_powers += digit ** power
    
    return sum_of_powers == number

number = int(input("Enter a number to check: "))
if is_disarium_number(number):
    print(f"{number} is a Disarium Number.")
else:
    print(f"{number} is not a Disarium Number.")