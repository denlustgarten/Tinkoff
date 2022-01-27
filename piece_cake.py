piece_cake = int(input())

number_of_cuts = 0
while piece_cake != 1:
    piece_cake = int(-1 * piece_cake // 2 * -1)
    number_of_cuts += 1

print(int(number_of_cuts))
