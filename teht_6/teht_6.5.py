def list(numbers):
    for n in numbers:
        if n % 2 != 0:
            numbers.remove(n)
    return numbers

number_list = [1, 2, 3, 4, 5]
print(number_list)
print(list(number_list))
