import matplotlib.pyplot as plt

influencers = ['A', 'B', 'C', 'D', 'E', 'F']
followers = [5, 8, 3, 10, 6, 7]

plt.barh(influencers, followers, color='skyblue')

plt.title('Instagram Influencers Followers')
plt.xlabel('Followers (in millions)')
plt.ylabel('Influencers')

plt.show()