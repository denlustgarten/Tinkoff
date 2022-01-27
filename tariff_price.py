input_data = input()
tariff_price, tariff_size, mb_price, user_size = map(int, input_data.split())

if tariff_size >= user_size:
    result_price = tariff_price
else:
    result_price = tariff_price + mb_price * (user_size - tariff_size)

print(result_price)