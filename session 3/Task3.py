import matplotlib.pyplot as plt

apps = ['Zomato', 'Swiggy', 'Uber Eats', 'Dunzo', "Domino's"]
orders = [150, 120, 90, 70, 110]

plt.bar(apps, orders, color='orange')

for i in range(len(apps)):
    plt.text(i, orders[i] + 2, str(orders[i]), ha='center')

plt.title('Daily Food Delivery Orders')
plt.xlabel('Food Delivery Apps')
plt.ylabel('Number of Orders')

plt.show()