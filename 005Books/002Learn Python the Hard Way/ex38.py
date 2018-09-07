states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])
# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
38
39
40 # print every city in state
print('-' * 10)
42 for abbrev, city in cities.items():
43
44
print "%s is abbreviated %s" % (state, abbrev)
print "%s has the city %s" % (abbrev, city)
# now do both at the same time
print('-' * 10)
47 for state, abbrev in states.items():
48 print "%s state is abbreviated %s and has city %s" % (
49
50
51
52 print '-' * 10
53 # safely get a abbreviation by state that might not be there
54 state = states.get('Texas', None)
state, abbrev, cities[abbrev])
55
56 if not state:
57 print "Sorry, no Texas."
58
59 # get a city with a default value
60 city = cities.get('TX', 'Does Not Exist')
61 print "The city for the state 'TX' is: %s" % city