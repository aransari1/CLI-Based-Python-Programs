#Maintainer: Abdurrahman Ansari
#Aim: To build a Temperature converter.

print(">>> Welcome to Temperature Converter <<<")

print ("Enter the unit you want to give input. \nHint:\nC for Censius\nF for Fahrenhiet\nK for Kelvin\nR for Rankine\nN for Newton\nRE for Réaumur")
Unit_Selection = input("Your input: ")

Desired_Unit_Selection = input("Enter the unit you want to convert into: ")

if Unit_Selection.isalpha():
    if Unit_Selection == ("c" or "C"):
        Print("Celsius (°C):\nCelsius is a commonly used temperature scale in which 0°C is the freezing point of water and 100°C is the boiling point of water at standard atmospheric pressure.")
        