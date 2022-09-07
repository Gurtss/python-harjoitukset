def list(numbers):
    num_list = numbers
    num = 0
    for n in num_list:
        num = num + n
    return num

number_list = [1, 2, 3, 4, 5]
total = list(number_list)
print(total)