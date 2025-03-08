def check_season(temp, unit):
    if unit == 'F' and temp == 31:
        return "Winter"
    elif unit == 'C' and temp == 31:
        return "Summer"
    else:
        return "Unknown season"

# Example usage
temperature = 31
unit = 'F'  # Change to 'C' for Celsius
season = check_season(temperature, unit)
print(f"The season is: {season}")