def main():
    """
    Main function that runs the temperature calculator.

    Example:
        Welcome to the Temperature Converter!

        Select input unit:
        1. Celsius
        2. Fahrenheit
        3. Kelvin

        Enter choice: 2
        Enter temperature in Fahrenheit: 68

        Select target unit:
        1. Celsius
        2. Kelvin

        Enter choice: 1

        Converted temperature: 20.0°C
    """
    print()
    print("Welcome to the Temperature Converter!")
    print()
    print("Select input unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    choice = input("Enter choice: ").strip()
    while choice not in ["1", "2", "3"]:
        print("Choose an integer between 1~3!")
        choice = input("Enter choice: ")

    choice2unit = {
        "1": "Celcius",
        "2": "Fahrenheit",
        "3": "Kelvin",
    }
    input_unit = choice2unit[choice]
    input_temp = input(f"Enter temperature in {input_unit}: ")
    while True:
        try:
            input_temp = float(input_temp)
            break
        except TypeError as te:
            print("Input temperature has to be a number!")
            input_temp = input(f"Enter temperature in {input_unit}: ")

    print()
    print("Select target unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = input("Enter choice: ").strip()
    while choice not in ["1", "2", "3"]:
        print("Choose an integer between 1~3!")
        choice = input("Enter choice: ")
    target_unit = choice2unit[choice]
    converted_temperature = convert_temperature(input_unit=input_unit, target_unit=target_unit, input_temp=input_temp)
    print()
    print(f"Converted temperature: {converted_temperature}")


def convert_temperature(input_unit: str, target_unit: str, input_temp: float):
    """Returns the stringified temperature with its unit, converted from input to target unit.

    Args:
        input_unit (str): the input temperature unit, chosen among "Celcius", "Fahrenheit", and "Kelvin"
        target_unit (str): the target temperature unit, chosen among "Celcius", "Fahrenheit", and "Kelvin"
        input_temp (float): the input temperature number

    Returns:
        converted_temperature (str): the converted temperature in string, with its unit attached

    Examples:
        convert_temperature(input_unit="Celcius", target_unit="Fahrenheit", input_temp=0) = "32.0°F"

    """
    target_symbol = f"°{target_unit[:1]}"  # First letter of unit is the symbol, e.g. Celcius = C
    if input_unit == target_unit:
        converted_temperature = f"{input_temp}{target_symbol}"

    elif input_unit == "Celcius":
        if target_unit == "Fahrenheit":
            converted_temperature = f"{str(celcius_to_fahrenheit(input_temp=input_temp))}{target_symbol}"
        else:  # target_unit == "Kelvin"
            converted_temperature = f"{str(celcius_to_kelvin(input_temp=input_temp))}{target_symbol}"

    elif input_unit == "Fahrenheit":
        if target_unit == "Celcius":
            converted_temperature = f"{str(fahrenheit_to_celcius(input_temp=input_temp))}{target_symbol}"
        else:  # target_unit == "Kelvin"
            converted_temperature = f"{str(fahrenheit_to_kelvin(input_temp=input_temp))}{target_symbol}"

    else:  # input_unit is Kelvin
        if target_unit == "Celcius":
            converted_temperature = f"{str(kelvin_to_celcius(input_temp=input_temp))}{target_symbol}"
        else:  # target_unit == "Fahrenheit"
            converted_temperature = f"{str(kelvin_to_fahrenheit(input_temp=input_temp))}{target_symbol}"

    return converted_temperature


def celcius_to_fahrenheit(input_temp: float):
    return input_temp * 9 / 5 + 32


def celcius_to_kelvin(input_temp: float):
    return input_temp + 273.15


def fahrenheit_to_celcius(input_temp: float):
    return (input_temp - 32) * 5 / 9


def fahrenheit_to_kelvin(input_temp: float):
    return celcius_to_kelvin(fahrenheit_to_celcius(input_temp))


def kelvin_to_celcius(input_temp: float):
    return input_temp - 273.15


def kelvin_to_fahrenheit(input_temp: float):
    return celcius_to_fahrenheit(kelvin_to_celcius(input_temp))

if __name__=="__main__":
    main()