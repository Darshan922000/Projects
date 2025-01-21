import pandas

'''data = pandas.read_csv("weather_data.csv")

dats_dict = data.to_dict()

temp_list = data["temp"].to_list()

average_temp = sum(temp_list) /  len(temp_list)
print("Average Temperature = ",average_temp)

maximum_value = data["temp"].max()
print(maximum_value)
print(data[data.temp == maximum_value])

monday = data[data.day == "Monday"]
temperature = monday.temp
farenheit_temperature = ((temperature * 1.8) + 32)
print(farenheit_temperature)'''

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnemon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur color":["Gray", "Cinnamon", "Black"],
    "color_count":[gray_color_count, cinnemon_color_count, black_color_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

