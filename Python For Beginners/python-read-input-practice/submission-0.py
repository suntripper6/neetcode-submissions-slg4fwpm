def add_two_numbers() -> int:
    numbers = input()
    two_nums = numbers.split(",")
    sum = 0

    for s in two_nums:
        sum += int(s)

    return sum


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
