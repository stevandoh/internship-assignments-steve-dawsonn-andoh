#create a mapping of state to abbreviations
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York': 'NY',
    'Michigan':'MI'
}

# create a basic set of states and some cities in them
cities = {'CA':'San Fransico',
    'MI':'Detroit',
    'FL':'Jacksonville'}
    


# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is:" , states['Michigan']
print "Florida's abbreviation is: " , states['Florida']

# do it by using the state then cities dict
print '-'* 10
print "Miichigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every city in state
print '-' * 10 
for state, abbrev in states.items():
    print "%s state in abbreviated %s and has city %s" %(
            state, abbrev, cities[abbrev])

# now do both at the same time
print '-' * 10 
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev,
        cities[abbrev])

print '-' * 10

#safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with default value
city = cities.get('TX','Does not exist')
print "The city for the state 'TX' is %s" % city

