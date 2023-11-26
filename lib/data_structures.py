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
    menuItem = [item["name"] for item in spicy_foods]
    return(menuItem)

def get_spiciest_foods(spicy_foods):
    spicy = (item for item in spicy_foods if item["heat_level"] > 5)
    return (spicy)

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(f'{item["name"]} ({item["cuisine"]}) | Heat Level: {item["heat_level"] * "🌶"}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item["cuisine"] == cuisine:
            return (item)

def print_spiciest_foods(spicy_foods):
    spicyItem = (dish for dish in spicy_foods if dish["heat_level"] > 5)
    for dish in spicyItem:
        print(f"{dish['name']} ({dish['cuisine']}) | Heat Level: {dish['heat_level'] * '🌶'} ")     

def get_average_heat_level(spicy_foods):
    hotContents = (item["heat_level"] for item in spicy_foods)
    sumHeat = 0
    for temp in hotContents:
        sumHeat = sumHeat + temp
    avgHeat = sumHeat / len(hotContents)
    return avgHeat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return(spicy_foods)
