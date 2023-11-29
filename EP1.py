# List: 
bikes = ['trek', 'redline', 'giant']
first_bike = bikes[0]
last_bike = bikes[-1]
# Looping through a list
for bike in bikes:
    print(bike)

# Adding items to a list
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')

# Making numerical list
squares = []
for x in range(1, 11):
    squares.append(x**2)
squares = [x**2 for x in range(1, 11)]
print(squares)

# Slicing a list
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(first_two)

#Tuples
dimensions = (1920, 1080)
print(dimensions)






