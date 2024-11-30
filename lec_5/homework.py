def sum_of_elements(numbers, exclude_negative=False):
    sum_numbers = 0
    for number in numbers:
        number = int(number)
        if exclude_negative:
            if number >= 0:
                sum_numbers += number
        else:
            sum_numbers += number
                
    return sum_numbers

numbers = input("Enter numbers separated by spaces: ").split()
input_exclude_negative = input("Do you want to exclude negative numbers (yes/no): ").strip().lower()
exclude_negative = input_exclude_negative == "yes"

result = sum_of_elements(numbers, exclude_negative)
print("Sum of elements:", result)
