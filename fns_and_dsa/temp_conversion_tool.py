# C to F conversion (9/5)
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# F to C conversion (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():    
    try:
        temp = input("Enter the temperature to convert: ")        
        try:
            temp_data = float(temp)
        except ValueError:
            raise ValueError("Invalid. Please enter a numeric value.")            
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            # Convert F to C
            temp_conversion = convert_to_celsius(temp_data)
            print(f"\nResult: {temp_data:.1f}°F is equal to {temp_conversion:.1f}°C.")
        elif unit == 'C':
            # Convert C to F
            temp_conversion = convert_to_fahrenheit(temp_data)
            print(f"{temp_data:.1f}°C is {temp_conversion:.1f}°F")
        else:
            print("\nError: Please enter 'C' or 'F'.")
            
    except ValueError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    main()
