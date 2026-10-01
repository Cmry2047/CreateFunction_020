def celsius_to_fahrenheit(celsius):
    """Converts a Celsius temperature to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Converts a Fahrenheit temperature to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#fahrenheit ke celcius
fahrenheit_temp = 105
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

#celcius ke fahrenheit
celsius_temp = 35
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp}°C")