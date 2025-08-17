def fahrenheit_celsius(f):
    return (f - 32) * 5/9 # °C
def celsius_fahrenheit(c):
    return (c * 9/5) + 32 # °F

while True :

  print("Unit Converter By @Seeleal13")
  print("==== MENU of available conversions ====")
  print("1) fahernheit to celius conversion")
  print("2) celsius to fahernheit conversion")
  print("press e to exit")

  menu_choice = input("choose by inserting a number from the Menu :")




  if menu_choice == "1" :
      
      f = float(input("enter the value of your temperature(°f) :"))

      conf = input(f"are u sure {f} is the value you want to convert ? (y/n)\n").lower()
      if conf == "y":
        print(f"{f} °f = {fahrenheit_celsius(f):.2f} °c")
        
      elif conf == "n":
        while conf == "n":
          f = float(input("enter the value of your temperature(°f) again :\n"))
          conf = input(f"are u sure {f} is the value you want to convert ? (y/n)\n").lower()
          if conf == "y":
            print(f"{f} °f = {fahrenheit_celsius(f):.2f} °c")
            break
          elif conf != "n" and conf != "y":
            print("invalid choice, make sure to enter y for yes or n for no \n SILLY USER :3 ")
        
      else:
        print("invalid choice, make sure to enter y for yes or n for no \n ")



  elif menu_choice == "2":
      
      c = float(input("enter the value of your temperature(°c) : "))

      conf = input(f"are u sure {c} is the value you want to convert ? (y/n): \n").lower()
      if conf == "y":
        print(f"{c} °c = {celsius_fahrenheit(c):.2f} °f")
        
      elif conf == "n":
        while conf == "n":
          c = float(input("enter the value of your temperature(°c) again :/ \n"))
          conf = input(f"are u sure {c} is the value you want to convert ? (y/n) \n").lower()
          if conf.lower() == "y":
            print(f"{c} °c = {celsius_fahrenheit(c):.2f} °f")
            break
          elif conf != "n" and conf != "y":
            print("invalid choice, make sure to enter y for yes or n for no \n SILLY USER :3 \n ")


      else:
        print("invalid choice, make sure to enter y for yes or n for no \n ")
        

  elif menu_choice == "e":
    break


  else:
      print("error: invalide choice \n")
    
    
      