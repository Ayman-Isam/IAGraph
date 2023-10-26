import matplotlib.pyplot as plt
import numpy as np

data = [2.10, 2.13, 2.92, 2.23, 2.29, 2.27, 2.67, 2.56, 2.32, 2.40, 2.84, 2.70, 2.84, 2.99, 2.76, 2.67, 3.10, 2.98, 2.64, 2.61, 2.74, 2.52, 2.62, 2.57, 2.38, 2.45, 2.15, 2.58]
colors = {
    'Mediterranean Avenue': 'brown',
    'Baltic Avenue': 'brown',
    'Reading Railroad': 'gray',
    'Oriental Avenue': 'lightblue',
    'Vermont Avenue': 'lightblue',
    'Connecticut Avenue': 'lightblue',
    'St. Charles Place': 'pink',
    'Electric Company': 'black',
    'States Avenue': 'pink',
    'Virginia Avenue': 'pink',
    'Pennsylvania Railroad': 'gray',
    'St. James Place': 'orange',
    'Tennessee Avenue': 'orange',
    'New York Avenue': 'orange',
    'Kentucky Avenue': 'red',
    'Indiana Avenue': 'red',
    'Illinois Avenue': 'red',
    'B&O Railroad': 'gray',
    'Atlantic Avenue': 'yellow',
    'Ventnor Avenue': 'yellow',
    'Water Works': 'black',
    'Marvin Gardens': 'yellow',
    'Pacific Avenue': 'green',
    'North Carolina Avenue': 'green',
    'Pennsylvania Avenue': 'green',
    'Short Line Railroad': 'gray',
    'Park Place': 'blue',
    'Boardwalk': 'blue',
}
properties = ['Mediterranean Avenue', 'Baltic Avenue', 'Reading Railroad', 'Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue', 'Pennsylvania Railroad', 'St. James Place', 'Tennessee Avenue', 'New York Avenue', 'Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue', 'B&O Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue', 'Short Line Railroad', 'Park Place', 'Boardwalk']

x = np.arange(len(data))

# Create the bar plot
plt.bar(x, data)

# Get the bar plot container objects
bars = plt.gca().containers[0]

# Set the color of each bar based on its property
for bar, prop in zip(bars, properties):
    bar.set_facecolor(colors[prop])

# Add labels to the bottom of the bars
plt.xticks(x, properties, rotation='vertical')

# Add title and axis labels
plt.title("Histogram of Property Revenue")
plt.xlabel("Property")
plt.ylabel("Probability")

# Display the plot
plt.tight_layout()

plt.show()
