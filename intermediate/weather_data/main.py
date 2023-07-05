import pandas

'''with open("intermediate/weather_data/data.csv") as file:
    contents = csv.reader(file)
    next(contents)
    days = []
    temperatures = []
    conditions = []
    for row in contents:
        days.append(row[0])
        temperatures.append(row[1])
        conditions.append(row[2])'''

data = pandas.read_csv("intermediate/weather_data/data.csv")

'''temp_list = data["Temperature"].to_list()
total = 0
for temp in temp_list:
    total += temp

average = total / len(temp_list)
print(average)'''

print(data['Temperature'].mean())
