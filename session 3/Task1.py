import matplotlib.pyplot as plt

apps = ['Zomato', 'Swiggy', 'Uber Eats', 'Dunzo', "Domino's"]
orders = [150, 120, 90, 70, 110]

colors = ['red', 'orange', 'green', 'blue', 'purple']

plt.bar(apps, orders, color=colors)

plt.title('Daily Food Delivery Orders')
plt.xlabel('Food Delivery Apps')
plt.ylabel('Number of Orders')

plt.show()