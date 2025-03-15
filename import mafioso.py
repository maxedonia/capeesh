#!/usr/bin/env python3
import random

def interleave_strings(s1, s2):
    """
    Randomly interleaves two strings while preserving the order
    of characters within each string.
    """
    i, j = 0, 0
    result = []
    while i < len(s1) or j < len(s2):
        if i < len(s1) and j < len(s2):
            if random.choice([True, False]):
                result.append(s1[i])
                i += 1
            else:
                result.append(s2[j])
                j += 1
        elif i < len(s1):
            result.append(s1[i])
            i += 1
        elif j < len(s2):
            result.append(s2[j])
            j += 1
    return "".join(result)

def main():
    # Prompt for user's name.
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # List of 15 Italian sandwiches with unique ingredients.
    sandwiches = [
        {"name": "The Caprese", "ingredients": "fresh mozzarella, tomato, basil, and a drizzle of balsamic glaze"},
        {"name": "The Meatball", "ingredients": "savory meatballs, marinara sauce, and melted provolone"},
        {"name": "The Sausage", "ingredients": "spicy sausage, sautéed peppers & onions, with a touch of marinara and mozzarella"},
        {"name": "The Prosciutto", "ingredients": "delicate prosciutto, arugula, creamy mozzarella, and a hint of fig jam"},
        {"name": "The Italian Stallion", "ingredients": "salami, ham, capicola, provolone, lettuce, and tomato"},
        {"name": "The Godfather", "ingredients": "roast beef, pepperoncini, provolone, and a generous spoon of giardiniera"},
        {"name": "The Sicilian", "ingredients": "grilled eggplant, zesty marinara, mozzarella, and fresh basil"},
        {"name": "The Roman", "ingredients": "turkey, crispy pancetta, lettuce, tomato, and garlic aioli"},
        {"name": "The Vesuvio", "ingredients": "spicy capocollo, pepperoncini, provolone, and a sprinkle of oregano"},
        {"name": "Mafia Special", "ingredients": "assorted deli meats, provolone, banana peppers, and Italian dressing"},
        {"name": "Don's Delight", "ingredients": "ham, salami, mortadella, provolone, with lettuce, tomato, and onions"},
        {"name": "Olive Branch", "ingredients": "black olive tapenade, mozzarella, roasted red peppers, and basil"},
        {"name": "The Capone", "ingredients": "corned beef, Swiss cheese, sauerkraut, and a slather of Russian dressing"},
        {"name": "The Bambino", "ingredients": "turkey, pesto, fresh spinach, and provolone cheese"},
        {"name": "The Underboss", "ingredients": "roast pork, provolone, broccoli rabe, and spicy giardiniera"}
    ]

    # Display the sandwich menu.
    print("\nChoose your Italian sandwich:")
    for i, sandwich in enumerate(sandwiches, start=1):
        print(f"{i}. {sandwich['name']}")
        print(f"   Ingredients: {sandwich['ingredients']}\n")

    # Get a valid sandwich choice.
    while True:
        try:
            choice = int(input("Enter the number corresponding to your sandwich choice (1-15): "))
            if 1 <= choice <= 15:
                break
            else:
                print("Please enter a number between 1 and 15.")
        except ValueError:
            print("That's not a valid number. Try again.")

    selected_sandwich = sandwiches[choice - 1]

    # Prepare strings for interleaving: combine first and last names, remove spaces from sandwich name.
    full_name_str = f"{first_name}{last_name}"
    sandwich_str = selected_sandwich["name"].replace(" ", "")

    # Create the buffoonish mix.
    buffoonish_mix = interleave_strings(full_name_str, sandwich_str)

    # Split the mix into two parts for a first and last name.
    split_index = (len(buffoonish_mix) + 1) // 2  # First half gets extra char if odd.
    buffoonish_first = buffoonish_mix[:split_index]
    buffoonish_last = buffoonish_mix[split_index:]

    # Final output.
    print("\nAlright, listen up...")
    print(f"You picked the '{selected_sandwich['name']}' sandwich, loaded with {selected_sandwich['ingredients']}.")
    print("Now, lemme see if I got yer name straight... (I'm tryin' to remember, capisce?)")
    print(f"Your buffoonish, gobbledygook name is: {buffoonish_first} {buffoonish_last}")
    print("Eh, that's what I got! You followin'?")

if __name__ == '__main__':
    main()
