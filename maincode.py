def fahrenheit_celsius(f):
    return (f - 32) * 5/9 # °C

def celsius_fahrenheit(c):
    return (c * 9/5) + 32 # °F

def get_conf(unit):
    while True:
        value = float(input(f"Enter the value of your temperature ({unit}): "))
        conf = input(f"Are you sure {value} is correct? (y/n): ").lower()
        if conf == "y":
            return value
        elif conf == "n":
            continue
        else:
            print("Invalid choice, enter y or n.")  

while True :

  print("Unit Converter By @Seeleal13")
  print("==== MENU of available conversions ====")
  print("1) °F to °C ")
  print("2) °C to °F")
  print("press e to exit \n")

  menu_choice = input("choose by inserting a number from the Menu :")


  if menu_choice == "1" :
      
      f = get_conf("°F")
      print(f"{f} °F = {fahrenheit_celsius(f):.2f} °C")

  elif menu_choice == "2":
    
    c = get_conf("°c")
    print(f"{c} °C = {celsius_fahrenheit(c):.2f} °F")

  elif menu_choice == "e":
    print("see u later !")
    break

  else:
      print("error: invalid choice \n")
    
    
      