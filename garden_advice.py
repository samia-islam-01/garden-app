# User input for season and plant type
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

season = input("Enter season (summer/winter): ").lower()
plant_type = input("Enter plant type (flower/vegetable): ").lower()

# Dictionary to hold gardening advice
advice = {
    "summer" : "Water your plants regularly and provide some shade.\n"
               "Recommended plants to plant in summer are Geranium and Salvias.\n",

    "winter" : "Protect your plants from frost with covers.\n"
               "Recommended plants to plant in winter are Primroses and Winter Jasmine.\n",

    "other_season" : "No advice for this season.\n",

    "flower" : "Use fertiliser to encourage blooms.\n"
               "Other methods to boost growth are re-potting and giving good access to water and light.",

    "vegetable" : "Keep an eye out for pests!\n"
                  "Try to use both barrier methods (e.g. insect mesh) and manual removal (e.g. hand picking off leaves)",

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


# Create a user personalised piece of advice
gardening_advice = season_advice(season)
gardening_advice += plant_advice(plant_type)

# Output this advice via logging
logging.info(gardening_advice)

# TODO: Possible features to add:
# - Add seasonal advice for autumn
# - Add seasonal advice for spring
# - Add advice for specific plants (e.g. Poppies or Daisies within flowers)