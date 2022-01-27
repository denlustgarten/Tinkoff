def digits(number: int):
    count = 0
    while number > 0:
        number = number//10
        count += 1
    return count


def update_number(numbers: list):
    numbers.sort()
    max_rank = digits(max(numbers))
    filter_arr = filter(lambda x: x // (10 ** (max_rank - 1)) > 0, numbers)
    old_val = min(filter_arr)
    new_val = 9 * 10 ** (max_rank - 1) + (old_val % (10 ** (max_rank - 1)))
    return old_val, new_val


numbers_amount, operation_num = map(int, input().split())
numbers_array = sorted(list(map(int, input().split())))
new_numbers_array = numbers_array.copy()


for i in range(operation_num):
    old_value, new_value = update_number(new_numbers_array[:])
    new_numbers_array[new_numbers_array.index(old_value)] = new_value

print(sum(new_numbers_array) - sum(numbers_array))

