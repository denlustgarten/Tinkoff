member_num = int(input())
gifts_distribution = list(map(int, input().split()))

number_count = [(x, gifts_distribution.count(x)) for x in range(1, member_num+1)]
not_one_santa = list(filter(lambda x: x[1] != 1, number_count))
if len(not_one_santa) == 2:
    if not_one_santa[0][1] == 2:
        print(not_one_santa[0][0], not_one_santa[1][0])
    else:
        print(not_one_santa[1][0], not_one_santa[0][0])
else:
    print(-1, -1)
