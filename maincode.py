def fahrenheit_celsius(f):
    return (f - 32) * 5/9 # °C

def celsius_fahrenheit(c):
    return (c * 9/5) + 32 # °F

def meters_kilometers(m):
    return m / 1000 # Km

def kilometers_meters(km):
    return km * 1000 # m

def grams_kilograms(g):
    return g / 1000 # Kg

def kilograms_grams(kg):
    return kg * 1000 # g

def get_conf(unit):
    while True:
        try:
            value = float(input(f"Enter the value of your unit ({unit}): "))
            conf = input(f"Are you sure {value} is correct? (y/n): ").lower()
            if conf == "y":
                return value
            elif conf == "n":
                continue
            else:
                print("silly user, only enter y or n.")  
        except ValueError:
            print("Invalid number, try again.")


while True:
    print("\n=== Unit Converter By @Seeleal13 ===")
    print("Main Menu (choose a category):")
    print("1) Temperature")
    print("2) Length")
    print("3) Weight")
    print("e) Exit\n")

    cate_choice = input("Choose category: ")

    if cate_choice == "1":  
        print("\n-- Temperature Conversions --")
        print("1) °F to °C")
        print("2) °C to °F")
        print("b) Back\n")

        menu_choice = input("Choose conversion: ")

        if menu_choice == "1":
            f = get_conf("°F")
            print(f"{f} °F = {fahrenheit_celsius(f):.2f} °C")
        elif menu_choice == "2":
            c = get_conf("°C")
            print(f"{c} °C = {celsius_fahrenheit(c):.2f} °F")
        elif menu_choice == "b":
            continue
        else:
            print("Invalid choice.")

    elif cate_choice == "2":  # Length
        print("\n-- Length Conversions --")
        print("1) m to km")
        print("2) km to m")
        print("b) Back`\n")

        menu_choice = input("Choose conversion: ")

        if menu_choice == "1":
            m = get_conf("m")
            print(f"{m} m = {meters_kilometers(m):.2f} km")
        elif menu_choice == "2":
            km = get_conf("km")
            print(f"{km} km = {kilometers_meters(km):.2f} m")
        elif menu_choice == "b":
            continue
        else:
            print("Invalid choice.")

    elif cate_choice == "3":  
        print("\n-- Weight Conversions --")
        print("1) g to kg")
        print("2) kg to g")
        print("b) Back")

        menu_choice = input("Choose conversion: ")

        if menu_choice == "1":
            g = get_conf("g")
            print(f"{g} g = {grams_kilograms(g):.2f} kg")
        elif menu_choice == "2":
            kg = get_conf("kg")
            print(f"{kg} kg = {kilograms_grams(kg):.2f} g")
        elif menu_choice == "b":
            continue
        else:
            print("Invalid choice.")

    elif cate_choice == "e":
        print("See u later, alligaror!")
        break
    else:
        print("Error: invalid choice.\n")
