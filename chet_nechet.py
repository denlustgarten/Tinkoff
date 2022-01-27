human_number = int(input())
human_line = list(map(int, input().split()))
human_line_with_number = list(enumerate(human_line, start=1))
wrong_place = list(filter(lambda x: sum(x) % 2 != 0, human_line_with_number))

if len(wrong_place) == 2 and wrong_place[0][0] % 2 != wrong_place[1][0]:
    print(wrong_place[0][0], wrong_place[1][0])
else:
    print(-1, -1)
