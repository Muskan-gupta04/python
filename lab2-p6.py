
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {fahrenheit}°F")
elif unit == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {celsius}°C")

