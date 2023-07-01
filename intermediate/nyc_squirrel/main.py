import pandas

data = pandas.read_csv('intermediate/nyc_squirrel/squirrel_data.csv')
fur = data['Primary Fur Color']
black = data[data['Primary Fur Color'] == 'Black']
gray = data[data['Primary Fur Color'] == 'Gray']
red = data[data['Primary Fur Color'] == 'Cinnamon']

fur_colors = {
    'Color': ["Black", "Gray", "Cinnamon", "Total"],
    'Amount': [len(black), len(gray), len(red), len(fur)]
}

new_data = pandas.DataFrame(fur_colors)
new_data.to_csv('intermediate/nyc_squirrel/new_squirrel_data.csv')