cities = ["london", "paris", "barcelona", "athens", "Casablanca"]

#filter city names longer than 5 characters( using filter and lambda )

long_city_names = filter(lambda city: len(city) > 5, cities)

# print(*long_city_names)

cap_long_city_names = list(map(lambda city : city.title(), long_city_names))

print(cap_long_city_names)

# All in one
clc = list(map(lambda city : city.title(), filter(lambda city: len(city) > 5, cities)))
print(clc)

# List comprehension alternative
cap_title_cities_compr = [city.title() for city in cities if len(city) > 5]
print(cap_title_cities_compr)