import numpy as np
import matplotlib.pyplot as plt



data = {'Magge':20, 'Biscuits':15, 'Toffee':30,
'Perfume':35,'Rasna':11}
items = list(data.keys())
values = list(data.values())

#fig = plt.figure(figsize = (10, 5))

plt.bar(items, values, color ='maroon')

plt.xlabel("Items available")
plt.ylabel("Quantity of items")
plt.title("Items and their quantities")
plt.show()