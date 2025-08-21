import os
import sys

def convert_value(value, conv_type, invert=False):
    conversions = {
        'fahrenheit_celsius': {'multiplier': 5/9, 'offset': -32, 'from_unit': '°F', 'to_unit': '°C'},
        'meters_kilometers': {'multiplier': 1/1000, 'from_unit': 'm', 'to_unit': 'km'},
        'grams_kilograms': {'multiplier': 1/1000, 'from_unit': 'g', 'to_unit': 'kg'}
    }
    conv = conversions.get(conv_type)
    if not conv:
        return "Error", "", ""
    if invert:
        multiplier = 1 / conv['multiplier']
        offset = -conv['offset'] / conv['multiplier'] if 'offset' in conv else 0
        from_unit, to_unit = conv['to_unit'], conv['from_unit']
    else:
        multiplier = conv['multiplier']
        offset = conv.get('offset', 0)
        from_unit, to_unit = conv['from_unit'], conv['to_unit']
    result = value * multiplier + offset
    return result, from_unit, to_unit

def get_conf(unit):
    while True:
        try:
            value = float(input(f"Enter the value of your unit ({unit}): "))
            if value < 0 and unit not in ['°F', '°C']:
                print("Value cannot be negative for this unit.")
                continue
            if unit not in ['°F', '°C'] and abs(value) > 1e6:
                print("Value is too large, try something smaller.")
                continue
            conf = input(f"Are you sure {value} is correct? (y/n): ").lower()
            if conf == "y":
                precision = input("Enter decimal places (0-5, default 2): ")
                try:
                    precision = int(precision) if precision else 2
                    if not 0 <= precision <= 5:
                        print("Precision must be between 0 and 5.")
                        continue
                except ValueError:
                    print("Invalid precision, using default (2).")
                    precision = 2
                return value, precision
            elif conf == "n":
                continue
            else:
                print("silly user, only enter y or n.")  
        except ValueError:
            print("Invalid number, try again.")

def clear_screen():
    os.system('cls' if sys.platform == 'win32' else 'clear')
def main():
    history = []

    while True:
        print("\n███████████████████████████████")
        print("█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█")
        print("█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█")
        print("█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█")
        print("█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████")
        print("█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████")
        print("█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████")
        print("█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████")
        print("█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████")
        print("█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█")
        print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█")
        print("█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█")
        print("███████████████████████████████")
        print("=== Unit Converter By @Seeleal13 ===")
        print("Main Menu (choose a category):")
        print("1) Temperature")
        print("2) Length")
        print("3) Weight")
        print("4) View History")
        print("e) Exit\n")

        cate_choice = input("Choose category: ")

        if cate_choice == "1":
            print("\n-- Temperature Conversions --")
            print("1) °F to °C")
            print("2) °C to °F")
            print("b) Back\n")

            menu_choice = input("Choose conversion: ")

            if menu_choice == "1":
                f, precision = get_conf("°F")
                result, from_unit, to_unit = convert_value(f, 'fahrenheit_celsius')
                if result != "Error":
                    print(f"{f} {from_unit} = {result:.{precision}f} {to_unit}")
                    history.append(f"{f} {from_unit} = {result:.{precision}f} {to_unit}")
                else:
                    print("Conversion error.")
                input("Press Enter to continue...")
                clear_screen()
            elif menu_choice == "2":
                c, precision = get_conf("°C")
                result, from_unit, to_unit = convert_value(c, 'fahrenheit_celsius', invert=True)
                if result != "Error":
                    print(f"{c} {from_unit} = {result:.{precision}f} {to_unit}")
                    history.append(f"{c} {from_unit} = {result:.{precision}f} {to_unit}")
                else:
                    print("Conversion error.")
                input("Press Enter to continue...")
                clear_screen()
            elif menu_choice == "b":
                clear_screen()
                continue
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
                clear_screen()

        elif cate_choice == "2":
            print("\n-- Length Conversions --")
            print("1) m to km")
            print("2) km to m")
            print("b) Back\n")

            menu_choice = input("Choose conversion: ")

            if menu_choice == "1":
                m, precision = get_conf("m")
                result, from_unit, to_unit = convert_value(m, 'meters_kilometers')
                if result != "Error":
                    print(f"{m} {from_unit} = {result:.{precision}f} {to_unit}")
                    history.append(f"{m} {from_unit} = {result:.{precision}f} {to_unit}")
                else:
                    print("Conversion error.")
                input("Press Enter to continue...")
                clear_screen()
            elif menu_choice == "2":
                km, precision = get_conf("km")
                result, from_unit, to_unit = convert_value(km, 'meters_kilometers', invert=True)
                if result != "Error":
                    print(f"{km} {from_unit} = {result:.{precision}f} {to_unit}")
                    history.append(f"{km} {from_unit} = {result:.{precision}f} {to_unit}")
                else:
                    print("Conversion error.")
                input("Press Enter to continue...")
                clear_screen()
            elif menu_choice == "b":
                clear_screen()
                continue
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
                clear_screen()

        elif cate_choice == "3":
            print("\n-- Weight Conversions --")
            print("1) g to kg")
            print("2) kg to g")
            print("b) Back\n")

            menu_choice = input("Choose conversion: ")

            if menu_choice == "1":
                g, precision = get_conf("g")
                result, from_unit, to_unit = convert_value(g, 'grams_kilograms')
                if result != "Error":
                    print(f"{g} {from_unit} = {result:.{precision}f} {to_unit}")
                    history.append(f"{g} {from_unit} = {result:.{precision}f} {to_unit}")
                else:
                    print("Conversion error.")
                input("Press Enter to continue...")
                clear_screen()
            elif menu_choice == "2":
                kg, precision = get_conf("kg")
                result, from_unit, to_unit = convert_value(kg, 'grams_kilograms', invert=True)
                if result != "Error":
                    print(f"{kg} {from_unit} = {result:.{precision}f} {to_unit}")
                    history.append(f"{kg} {from_unit} = {result:.{precision}f} {to_unit}")
                else:
                    print("Conversion error.")
                input("Press Enter to continue...")
                clear_screen()
            elif menu_choice == "b":
                clear_screen()
                continue
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
                clear_screen()

        elif cate_choice == "4":
            print("\n-- Conversion History --")
            if history:
                for i, entry in enumerate(history, 1):
                    print(f"{i}. {entry}")
            else:
                print("No conversions yet.")
            input("Press Enter to continue...")
            clear_screen()

        elif cate_choice == "e":
            print("See u later, alligator!")
            break
        else:
            print("Error: invalid choice.")
            input("Press Enter to continue...")
            clear_screen()

if __name__ == "__main__":
    main()