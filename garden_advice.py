# User input for season and plant type
season = input("Enter season: ").lower()  # TODO: Replace with input() to allow user interaction.
plant_type = input("Enter plant type: ").lower()  # TODO: Replace with input() to allow user interaction.

# Dictionary to hold gardening advice
advice = {
    "summer" : "Water your plants regularly and provide some shade.\n"
               "Recommended plants to plant in summer are Geranium and Salvias.\n",
    "winter" : "Protect your plants from frost with covers.\n"
               "Recommended plants to plant in winter are Primroses and Winter Jasmine.\n",
    "other_season" : "No advice for this season.\n",
    "flower" : "Use fertiliser to encourage blooms.\n",
    "vegetable" : "Keep an eye out for pests!\n",
    "other_plant" : "No advice for this plant.\n"
}


def season_advice(season):
    """Determine advice based on the season"""
    user_advice = ""

    if season == "summer":
        user_advice += advice["summer"]
    elif season == "winter":
        user_advice += advice["winter"]
    else:
        user_advice += advice["other_season"]

    return user_advice


def plant_advice(plant_type):
    """Determine advice based on the plant type"""
    user_advice = ""

    if plant_type == "flower":
        user_advice += advice["flower"]
    elif plant_type == "vegetable":
        user_advice += advice["vegetable"]
    else:
        user_advice += advice["other_plant"]

    return user_advice


# Print the personalised advice
print(f"Your advice for gardening in {season}: {season_advice(season)}")
print(f"Your advice for gardening {plant_type}: {plant_advice(plant_type)}")