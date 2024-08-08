import csv
from random import random

# Load colognes from CSV
def load_colognes(filename):
    colognes = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        headers = next(spamreader)
        for row in spamreader:
            cologne = {headers[index]: row[index].strip() for index in range(len(headers))}
            colognes.append(cologne)

    for cologne in colognes:
        if cologne["Price"] == "":
            cologne["Price"] = 99999999999   
        cologne["Price"] = int(cologne["Price"])
        if cologne["Intensity"] == "":
            cologne["Intensity"] = -1
        cologne["Intensity"] = int(cologne["Intensity"])
    return colognes

# Function to filter colognes 
def filter_colognes(
    colognes, 
    min_price=None, 
    max_price=None, 
    scent_family_1=None,
    scent_family_2=None, 
    intensity_list=None
    ):

    return [
        cologne for cologne in colognes
        if (min_price is None or int(cologne["Price"]) >= min_price) and 
        (max_price is None or int(cologne["Price"]) <= max_price) and
        (scent_family_1 is None or cologne["Scent_Family"] == scent_family_1) and
        (scent_family_2 is None or cologne["Scent_Family_2"] == scent_family_2) and 
        (intensity_list is None or cologne["Intensity"] in intensity_list) 
    ]

# Sort by price 
def sort_by_price(colognes):
    def get_price(cologne):
        return cologne["Price"]
    colognes.sort(key=get_price, reverse=True)

# Sort by Name (alphabetically)
def sort_by_name(colognes):
    def get_name(cologne):
        return cologne["Name"]
    colognes.sort(key=get_name)

# List of Scent Families
def get_scent_family_list(colognes):
    scent_family_list = []
    for cologne in colognes:
        if cologne["Scent_Family"] not in scent_family_list:
            scent_family_list.append(cologne["Scent_Family"])
    return scent_family_list

# List of Scent Families 2
def get_scent_family_list2(colognes):
    scent_family_list_2 = []
    for cologne in colognes:
        if cologne["Scent_Family_2"] not in scent_family_list_2:
            scent_family_list_2.append(cologne["Scent_Family_2"])
    return scent_family_list_2

# Function to print cologne details
def print_cologne(cologne):
    print()
    print(f'Name: {cologne["Name"]}')
    print(f'Description: {cologne["Description"]}')
    print(f'Price: ${cologne["Price"]}')
    print(f'Scent Family: {cologne["Scent_Family"]} - {cologne["Scent_Family_2"]}')
    intensity_dict = {
        -1: "Blank",
        1: "Eau fraiche",
        2: "Eau De Cologne",
        3: "Eau De Toilette",
        4: "Eau De Parfum",
        5: "Parfum",
    }
    print(f'Intensity: {intensity_dict[cologne["Intensity"]]}')
    print(f'Website Link: {cologne["Website_Link"]}')
    print()

# Intensity Range / Checker
def intensity_range(): 
    while True: 
        user_input_string = input("Choose an intensity level or range (Format must either be '1' or '1-5'): ")

        user_input_list = user_input_string.split("-")
        if len(user_input_list) == 1:
            min_string = user_input_list[0]
            max_string = min_string
        elif len(user_input_list) == 2:
            min_string = user_input_list[0]
            max_string = user_input_list[1]
        else:
            print("Too many dashes! Please enter a valid range.")
            continue

        try:
            min_intensity = int(min_string)
            max_intensity = int(max_string)
        except ValueError:
            print("Input couldn't be interpreted as an integer. Please enter valid numbers.")
            continue

        if min_intensity > max_intensity:
            print("Minimum intensity is greater than maximum intensity. Please enter a valid range.")
            continue

        if min_intensity < 1 or max_intensity > 5:
            print("Intensity must be in the range of 1-5. Please enter a valid range.")
            continue

        break
 
    user_input_range = range(min_intensity, max_intensity + 1) 

    return user_input_range

# Function to print Menu
def print_menu(options: list[str], descriptions={}): # Options is supposed to be a list of strings 
    for index in range(len(options)):
        print(f"{index}: {options[index]}", end="")
        if options[index] in descriptions:
            print(f" - {descriptions[options[index]]}", end="")
        print()
    print()  # Add a blank line for spacing

    while True:
        user_pick = input("Choose an option: ")
        try:
            pick_index = int(user_pick)
        except ValueError:
            if user_pick in options:
                pick_index = options.index(user_pick)
            else:
                print("Please enter a valid value (either number or option).")
                print()
                continue
        if 0 <= pick_index < len(options):
            return pick_index, options[pick_index]
        print("Please choose something within the range!")
        print()

# Returns a list of 4 random colognes 
def rand_cologne(colognes, num=4):
    if len(colognes) < num: 
        return colognes
    
    random_4 = []
    while len(random_4) < num:
        random_cologne_index = int(random() * len(colognes))
        appended_cologne = colognes[random_cologne_index]

        if appended_cologne not in random_4:
            random_4.append(appended_cologne)
    return random_4

def main():
    All_colognes = load_colognes('Cologne_dataset.csv')  
    colognes = All_colognes
    descriptions = {
        "Woody": "Warm and earthy, resembling the smell of woods like cedar, sandalwood, and pine. Perfect for a grounded and robust fragrance.",
        "Ambery": "Rich and warm, with sweet and resinous notes of amber, vanilla, and spices. Conveys a cozy and luxurious feel.",
        "Aromatic Fougere": "Fresh and aromatic, blending herbs, lavender, and woods. Offers a classic and refined scent.",
        "Citrus": "Fresh and zesty, reminiscent of lemon, lime, and orange. Perfect for a clean and invigorating feel.",
        "Leather": "Deep and masculine, reminiscent of tanned leather and suede. Perfect for a sophisticated and rugged touch.",
        "Floral": "Soft and romantic, like a bouquet of fresh flowers such as roses, jasmine, and lilies.",
        "Chypre": "Complex and elegant, combining citrus, oakmoss, and patchouli. Offers a sophisticated and timeless scent.",
        "Watery": "Light and refreshing, reminiscent of ocean breezes and fresh rain. Ideal for a clean and airy scent.",
        "Fruity": "Vibrant and sweet, filled with juicy notes like apple and berry. Perfect for a lively and playful aroma.",
        "Spicy": "Warm and bold, featuring pepper, clove, and cardamom. Great for a dynamic and invigorating touch.",
        "Musk Skin": "Soft and sensual, with intimate musk notes. Ideal for a warm and enveloping scent.",
        "Gourmand": "Sweet and indulgent, inspired by vanilla, chocolate, and caramel. Perfect for a delectable and comforting aroma.",
        "Green": "Fresh and natural, capturing lush foliage and herbs. Ideal for a clean and vibrant scent.",
        "Aldehydic": "Sparkling and clean, with crisp, soapy, and metallic notes. Perfect for a sophisticated and effervescent touch.",
        "Tobacco": "Rich and aromatic, featuring warm, smoky tobacco notes. Ideal for a timeless and elegant scent.",
        }
        
    user_input_min_price = None
    user_input_max_price = None
    user_intensity_range = None
    SF1_sort = None
    SF2_sort = None

    def filter_display():
        print()
        if user_input_min_price != None: 
            print(f'Price range: {user_input_min_price} - {user_input_max_price}')
        if user_intensity_range != None: 
            print(f'Intensity range: {user_intensity_range.start} - {user_intensity_range.stop-1}')
        if SF1_sort != None: 
            print(f'Primary Scent Family: {SF1_sort}')
        if SF2_sort != None: 
            print(f'Secondary Scent Family: {SF2_sort}')



    while True: 
        options = [
            "Preview Cologne Selection", 
            "Filter By Price",
            "Filter by Intensity",
            "Filter by Primary Scent Family",
            "Filter by Secondary Scent Family",
            "Reset Filter",
            "Quit Program"
        ]
        
        print("\nPlease choose an option from the menu:")
        _, choices = print_menu(options)
        
        if choices == "Preview Cologne Selection":        
            sort_by_name(colognes)
            sort_by_price(colognes)
            print(f"\nNumber of colognes found: {len(colognes)}")
            if colognes:
                random_colognes = rand_cologne(colognes)
                for cologne in random_colognes:
                    print_cologne(cologne)
                if len(colognes) > 4:
                    more = input("Would you like to see the entire list? (yes/no): ")
                    if more.lower() == "yes":
                        for cologne in colognes:
                            print_cologne(cologne)

        if choices == "Filter By Price": 
            try:
                user_input_min_price = int(input("\nWhat is your min price? "))
                user_input_max_price = int(input("What is your max price? "))
            except ValueError:
                print("Please enter a valid number for price.")
                continue
            colognes = filter_colognes(
                All_colognes,
                min_price=user_input_min_price,
                max_price=user_input_max_price,
                intensity_list=user_intensity_range,
                scent_family_1=SF1_sort,
                scent_family_2=SF2_sort
            )
            print(f"\nNumber of colognes found: {len(colognes)}")
            filter_display()


        if choices == "Filter by Intensity": 
            user_intensity_range = intensity_range()
            colognes = filter_colognes(
                All_colognes,
                min_price=user_input_min_price,
                max_price=user_input_max_price,
                intensity_list=user_intensity_range,
                scent_family_1=SF1_sort,
                scent_family_2=SF2_sort
            )
            print(f"\nNumber of colognes found: {len(colognes)}")
            filter_display()

        if choices == "Filter by Primary Scent Family": 
            sfl = get_scent_family_list(colognes)
            _, SF1_sort = print_menu(sfl, descriptions)
            colognes = filter_colognes(
                All_colognes,
                min_price=user_input_min_price,
                max_price=user_input_max_price,
                intensity_list=user_intensity_range,
                scent_family_1=SF1_sort,
                scent_family_2=SF2_sort
            )
            print(f"\nNumber of colognes found: {len(colognes)}")
            filter_display()
    
        if choices == "Filter by Secondary Scent Family": 
            sfl2 = get_scent_family_list2(colognes)
            _, SF2_sort = print_menu(sfl2, descriptions)
            colognes = filter_colognes(
                All_colognes,
                min_price=user_input_min_price,
                max_price=user_input_max_price,
                intensity_list=user_intensity_range,
                scent_family_1=SF1_sort,
                scent_family_2=SF2_sort
            )
            print(f"\nNumber of colognes found: {len(colognes)}")
            filter_display()

        if choices == "Reset Filter": 
            user_input_min_price = None
            user_input_max_price = None
            user_intensity_range = None
            SF1_sort = None
            SF2_sort = None
            colognes = All_colognes
            print("\nFilters have been reset.")

        if choices == "Quit Program": 
            print("\nThank you for using the program. Goodbye!")
            break
       
if __name__ == "__main__":
    main()
