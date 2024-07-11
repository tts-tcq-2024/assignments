import re

def add(number_string):
    numbers = re.findall(r'\d+', number_string)
    number_list = [int(number) for number in numbers if int(number) < 1000]
    return sum(number_list)

# Example usage
example_string = "The total is 100 and the discount is 50. Add 52 and 999."
result = add(example_string)
print(f"The sum of numbers less than 1000 is: {result}")
