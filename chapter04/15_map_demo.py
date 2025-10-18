cities = ["london", "paris", "athens", "barcelona"]

# filter() -> returns some of the list elements if the obey the predicate
# map() -> returns all the elements inside a list but changed
cap_cities = list(map(lambda city: city.title(), cities))

print(f"Cap cities: {cap_cities}")