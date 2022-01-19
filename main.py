with open("weather_data.csv") as weather_data:
    data = weather_data.read().splitlines()

print(data)