
# string format,f`string
x=["test23", "test2", "test3"]
print (f'this is fstr text inside x var - {x}')
print (('this is regular text inside x var: '), (x))
# print (lista)



# split method
txt='askdljh,,kljhqwe,,aasdf'
arr =(txt.split(',,'))
lista = txt.split(',,')

print (txt,"; after split:", arr)

# digits in int/string
numb=1234567899
for i in str(numb):
	print(int(i), end=(' '))
print ()

# list / tuples / unpack
file_info=('notes','txt',496)
name, ext, size = file_info
print("{:.2f}".format(size / 1024))

# enumerate() returns a two-element tuple of the current list item and its position in the list.
def skip_elements(elements):
    element = []
    for i, e in enumerate(elements):
        if i % 2 == 0: # every 2nd
            element.append(e)
    return element
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']

# list comprehensions
vec = [2, 4, 6]
multiples = [3*x for x in vec]

nn = 33
print ([x for x in range(1,nn+1) if x%3==0])

# ---
Weather = "Rainfall"; y=10
print(Weather[:4])
print (y)

# assignment list
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result+='-'
    return result


# dictionaries

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item,colors in wardrobe.items():
	# print (item)
	for color in colors:
		print("{} {}".format(color, item))

# ass dict
def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+"@"+domain)
	return(emails)

# 
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group,users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			# groups for this user, creating the entry
			# in the dictionary if necessary
			user_groups[user] = user_groups.get(user,[]) + [group]
	return(user_groups)

# 
groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
def add_prices(basket):
	total = 0
	for item,price in basket.items():
		total += price
	return round(total, 2)
	# return round(sum(basket.values()), 2) # one liner !!!
print(add_prices(groceries)) # Should print 28.44


## OBJ ORIENT PROG ##

class Flower: # define a class
  color = 'unknown' #define an attrib
rose = Flower() # set var as class
rose.color = 'red' #in class define .color attrib
violet = Flower()
violet.color = 'blue'
print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0
# create a new instance of the City class and define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509
def max_elevation_city(min_population):
	# Initialize the variable that will hold the information of the city with the highest elevation 
	return_city = City()
  # Evaluate the 1st instance to meet the requirements: does city #1 have at least min_population and is its elevation the highest evaluated so far?
	if city1.population>=min_population and city1.elevation>return_city.elevation:
		return_city = city1
	if city2.population>=min_population and city2.elevation>return_city.elevation:
		return_city = city2
	if city3.population>=min_population and city3.elevation>return_city.elevation:
		return_city = city3
  #Format the return string
	if return_city.name:
		return ("{}, {}".format(return_city.name,return_city.country))
	else:
		return ""
print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

# 
class Furniture:
	color = ""
	material = ""
table = Furniture()
table.color='brown'
table.material='wood'
couch = Furniture()
couch.color='red'
couch.material='leather'
def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))
print(describe_furniture(table)) # Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) # Should be "This piece of furniture is made of red leather"

# or
class Furniture:
    color = ""
    material = ""
    def describe(self):
        return ("This piece of furniture is made of {} {}".format(self.color, self.material))
table = Furniture()
table.color='brown'
table.material='wood'
couch = Furniture()
couch.color='red'
couch.material='leather'
print(table.describe()) # Should be "This piece of furniture is made of brown wood"

# Calling methods on objects executes functions that operate on attributes of a specific instance of the class. This means that calling a method on a list, for example, only modifies that instance of a list, and not all lists globally. We can define methods within a class by creating functions inside the class definition. These instance methods can take a parameter called self which represents the instance the method is being executed on. This will allow you to access attributes of the instance using dot notation, like self.name, which will access the name attribute of that specific instance of the class object. When you have variables that contain different values for different instances, these are called instance variables.
class Dog:
  years = 0
  def dog_years(self):
    return self.years*7
fido=Dog()
fido.years=3
print(fido.dog_years())

# constructor metods # docstrings
class Person:
    def __init__(self, name): # constructor
        self.name = name
    def greeting(self):
     """Outputs a message with the name of the person -- docstring"""
       return ("hi, my name is {}".format(self.name)) 
help(Person)
# Create a new instance with a name of your choice
some_person = Person("Wlodo")
# Call the greeting method
print(some_person.greeting()) # dont forget ()

# 
class Apple:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor
	def __str__(self):
		return "This apple is {} and its flavor is {}".format(self.color, self.flavor) # __str__ create method exec via print
jonagold = Apple("red", "sweet")
print(jonagold) # >> This apple is red and its flavor is sweet

# inheritance / nested classes
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

# difficult
class Clothing:
   stock={ 'name': [],'material' :[], 'amount':[]}
   def __init__(self,name):
     material = ""
     self.name = name
   def add_item(self, name, material, amount):
     Clothing.stock['name'].append(self.name)
     Clothing.stock['material'].append(self.material)
     Clothing.stock['amount'].append(amount)
   def Stock_by_Material(self, material):
     count=0
     n=0
     for item in Clothing.stock['material']:
       if item == material:
         count += Clothing.stock['amount'][n]
         n+=1
     return count
   def Stock_by_item(self, name):
     count=0
     n=0
     for rec in Clothing.stock['name']:
       if rec == name:
         count += Clothing.stock['amount'][n]
         n+=1
     return count

class shirt(Clothing):
   material="Cotton"
class pants(Clothing):
   material="Cotton"

polo = shirt("Polo")
other_polo_shirts = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
other_polo_shirts.add_item(other_polo_shirts.name, other_polo_shirts.material, 16)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_item("Polo")
print(current_stock)

# import modules / Py Standard Library
import datetime
now = datetime.datetime.now()
type(now)
print(now)
now.year
print(now + datetime.timedelta(days=28))

# ooo lab
class Animal:
    name = ""
    category = ""
    def __init__(self, name):
        self.name = name
    def set_category(self, category):
        self.category = category
class Zoo:
    def __init__(self):
        self.current_animals = {}
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()
turtle = Animal("Turtle") #create an instance of the Turtle class
turtle.set_category('reptile')
snake = Animal("Snake") #create an instance of the Snake class
snake.set_category('reptile')

zoo.add_animal(turtle)
zoo.add_animal(snake)
print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category

# oo lab
#Begin Portion 1#
import random
class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}
    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load
    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]
    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for load in self.connections.values():
            total += load
        # Add up the load for each of the connections
        return total
    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())    
#End Portion 1#
server = Server()
server.add_connection("192.168.1.1")
print(server.load())
#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]
    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()
    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)
                break
    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        total_server = 0
        for server in self.servers:
            total_load += server.load()
            total_server += 1
        return total_load/total_server
    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())
    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2
 
 # Practice Notebook - Putting It All Together
 class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
def get_event_date(event):
    return event.date
def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and machines[event.machine] == event.user:
            machines[event.machine].remove(event.user)
    return machines
def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))
events = [Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),]
users = current_users(events)
print(users)
generate_report(users)

# FINAL ASSIGNMENT
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]  
# LEARNER CODE START HERE
file = "If your word cloud image did not appear, go back and rework your calculate_frequencies function until you get the desired output. Definitely check that you passed your frequecy count dictionary into the generate_from_frequencies function of wordcloud. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!"   
words=file.split()
result={}
for word in words:
    if word.lower() not in uninteresting_words:
        for letter in word:
            if letter in punctuations:
                letter.replace(punctuations,"")
        if word not in result.keys():
            result[word]=1
        else:
            result[word]+=1
print(result)

# option, own version
result=str()
for letter in file.lower():
    if letter in punctuations:
        letter=""
    result+=letter
words=result.split()
for word in words:
    if word in uninteresting_words:
        print(word)
        words.remove(word)
counted=0
results={}
for word in words:
    counted=result.count(word)
    results[word]=counted
print (results)