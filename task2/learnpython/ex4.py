# car number
cars = 100
#number of seat available
space_in_car = 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
#number of cars not driver
cars_not_driven = cars - drivers
# if there is a driver then a car is driven
cars_driven = drivers
#number of seat * the number of car driven
carpool_capacity = cars_driven * space_in_car
# average passengers per car
average_passengers_per_car = passengers / cars_driven

print "There are ", cars , "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."