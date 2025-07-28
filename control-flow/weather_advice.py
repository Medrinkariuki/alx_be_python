<<<<<<< HEAD
# weather_advice.py

# Ask the user for the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations based on input
=======
# File: weather_advice.py

# Prompt the user for input
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Decision logic using conditional statements
>>>>>>> 0376ac8a62ed838d642c560f32e8d9af6701bd92
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
