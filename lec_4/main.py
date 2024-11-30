numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List of numbers:", numbers)
even = []
odd = []

def classify_numbers(number):
    for num in number:
        if num % 2 == 0:
            even.append(num)
        elif num % 2== 1:
            odd.append(num)

    return even, odd

zuyg, kent =classify_numbers(numbers)

print(zuyg)
print(kent)
