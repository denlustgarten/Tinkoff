number_of_cities = int(input())

roads_array = []
for i in range(number_of_cities):
    roads = input()
    arr = [int(x) for x in roads.split()]
    roads_array.append(arr)
print(roads_array)

number_of_road = 0
city_numb = 1

for roads_to_city in roads_array:
    number_of_road += sum(roads_to_city[city_numb:])
    city_numb += 1

print(number_of_road)