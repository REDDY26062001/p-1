def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    print(f"Output: {positive_numbers}")


input_str1 = input("Enter a list of numbers (comma-separated): ")
list1 = [int(num) for num in input_str1.split(',')]

input_str2 = input("Enter another list of numbers (comma-separated): ")
list2 = [int(num) for num in input_str2.split(',')]


print("\nInput:", list1)
print_positive_numbers(list1)

print("\nInput:", list2)
print_positive_numbers(list2)
