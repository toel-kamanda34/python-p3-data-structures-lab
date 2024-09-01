spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food["heat_level"] >5]
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine", None) == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    number_of_foods = len(spicy_foods)
    average_heat_level =int(total_heat_level / number_of_foods )
    return average_heat_level
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)