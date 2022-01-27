
employer_number, leave_time = map(int, input().split())
floor_list = list(map(int, input().split()))
employ_who_leave = int(input())

len_lowest_to_highest = max(floor_list) - min(floor_list)
leave_employ_floor = floor_list[employ_who_leave - 1]

if (max(floor_list) - leave_employ_floor) <= leave_time or \
        (leave_employ_floor - min(floor_list)) <= leave_time:
    stairway_number = len_lowest_to_highest
elif leave_employ_floor <= len_lowest_to_highest / 2 + min(floor_list):
    stairway_number = (leave_employ_floor - min(floor_list)) + len_lowest_to_highest
else:
    stairway_number = (max(floor_list) - leave_employ_floor) + len_lowest_to_highest

print(stairway_number)


