"""Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile".
Call your function with at least three city-country pairs, and print the values that are returned."""

def city_country(ciudad, pais):
    return f"{ciudad}, {pais}"

print(city_country("Bogota", "Colombia"))
print(city_country("CDM", "Mexico"))
print(city_country("Caracas", "Venezuela"))