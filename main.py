# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
#
# monday_temp_f = monday_temp * 9 / 5 + 32
# print(monday_temp_f)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("student_scores.csv")
# print(data)
data = pandas.read_csv("2018_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
fur_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(black_squirrels), len(cinnamon_squirrels)]
}

df = pandas.DataFrame(fur_dict)
df.to_csv("squirrel_count.csv")

print((fur_dict))
