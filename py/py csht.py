---
## String Reference Cheat Sheet
String operations
len(string) #Returns the length of the string
for character in string #Iterates over each character in the string
if substring in string #Checks whether the substring is part of the string
string[i] #Accesses the character at index i of the string, starting at zero
string[i:j] #Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.
for index, element in enumerate(sequence) #Iterates over both the indexes and the elements in the sequence at the same time

String methods
string.lower() / string.upper() #Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() #Returns a copy of the string without left / right / left or right whitespace
string.count(substring) #Returns the number of times substring is present in the string
string.isnumeric() #Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() #Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) #Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) #Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) #Returns a new string with all the strings joined by the delimiter 

# more:
https://docs.python.org/3/library/stdtypes.html#string-methods

---  
## Formatting expressions
# "base string with {} placeholders".format(variables)
example = "format() method"
formatted_string = "this is an {} on a string".format(example)
print(formatted_string)

# "{0} {1}".format(first, second)
first = "apple"; second = "banana"; third = "carrot"
formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)

# If the placeholders indicate a field name, they’re replaced by the variable corresponding to that field name. This means that parameters to format need to be passed indicating the field name.
"{var1} {var2}".format(var1=value1, var2=value2)

# f-strings
item = "Purple Cup"
amount = 5
price = amount * 3.25
print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')

# If the placeholders include a colon, what comes after the colon is a formatting expression.
# {:d} integer value
'{:d}'.format(10.5) → '10'

Expr | Meaning | Example
{:d} | integer value | '{:d}'.format(10.5) → '10'
{:.2f} | floating point with that many decimals | '{:.2f}'.format(0.5) → '0.50'
{:.2s} | string with that many characters | '{:.2s}'.format('Python') → 'Py'
{:<6s} |string aligned to the left that many spaces | '{:<6s}'.format('Py') → 'Py    '
{:>6s} | string aligned to the right that many spaces | '{:>6s}'.format('Py') → '    Py'
{:^6s} | string centered in that many spaces | '{:^6s}'.format('Py') → '  Py  '

# more: 
https://docs.python.org/3/library/string.html#format-specification-mini-language

## Lists and Tuples Operations Cheat Sheet

# List-specific operations and methods:
list[i] = x #Replaces the element at index i with x
list.append(x) #Inserts x at the end of the list
list.insert(i, x) #Inserts x at index i
list.pop(i) #Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
list.remove(x) #Removes the first occurrence of x in the list
list.sort() #Sorts the items in the list
list.reverse() #Reverses the order of items of the list
list.clear() #Removes all the items of the list
list.copy() #Creates a copy of the list
list.extend(other_list) #Appends all the elements of other_list at the end of list


##  DICTIONARY
#Dictionary Methods Cheat Sheet
x = {key1:value1, key2:value2} 

Operations
len(dictionary) #Returns the number of items in the dictionary
for key in dictionary #Iterates over each key in the dictionary
for key, value in dictionary.items() #Iterates over each key,value pair in the dictionary
if key in dictionary #Checks whether the key is in the dictionary
dictionary[key] #Accesses the item with key key of the dictionary
dictionary[key] = value #Sets the value associated with key
del dictionary[key] #Removes the item with key key from the dictionary

# Methods
dict.get(key, default) #Returns the element corresponding to key, or default if its not present
dict.keys() #Returns a sequence containing the keys in the dictionary
dict.values() #Returns a sequence containing the values in the dictionary
dict.update(other_dictionary) #Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
dict.clear() #Removes all the items of the dictionary

# Converting a List of Tuples to a Dictionary
color=[('red',1),('blue',2),('green',3)]
d=dict(color)
print (d) #Output:{'red': 1, 'blue': 2, 'green': 3}

# Converting a List of Alternative Key, Value Items to a Dictionary
l1=[1,'a',2,'b',3,'c',4,'d']
l2=l1[::2] #Creating list containing keys alone by slicing
l3=l1[1::2] #Creating list containing values alone by slicing
z=zip(l2,l3) #merging two lists uisng zip()
print (dict(z)) #Converting zip object to dict using dict() constructor.
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Converting a List of Dictionaries to a Single Dictionary
l1=[{1:'a',2:'b'},{3:'c',4:'d'}]
d1={}
for i in l1:
    d1.update(i)
print (d1) #Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Converting a List to a Dictionary Using Enumerate()
l1=['a','b','c','d']
d1=dict(enumerate(l1))
print (d1) #Output:{0: 'a', 1: 'b', 2: 'c', 3: 'd'}

# Converting List Into a Dictionary Using Dictionary Comprehension
l1=[1,2,3,4]
d1={k:"a" for k in l1}
print (d1) #Output:{1: 'a', 2: 'a', 3: 'a', 4: 'a'}

# Converting a List to a Dictionary Using dict.fromkeys()
l1=['red','blue','orange']
d1=dict.fromkeys(l1,"colors")
print (d1) #Output:{'red': 'colors', 'blue': 'colors', 'orange': 'colors'}

# Converting a Nested List to a Dictionary Using Dictionary Comprehension
list1 = [[1,2],[3,4],[5,[6,7]]]
d1={x[0]:x[1] for x in list1}
print(d1) #Output:{1: 2, 3: 4, 5: [6, 7]}


# Classes and Methods Cheat Sheet
class ClassName:
    """Documentation for the class."""
    def method_name(self, other_parameters):
        """Documentation for the method."""
        body_of_method
        
def function_name(parameters):
    """Documentation for the function."""
    body_of_function

Classes and Instances
Classes define the behavior of all instances of a specific class.
Each variable of a specific class is an instance or object.
Objects can have attributes, which store information about the object.
You can make objects do work by calling their methods.
The first parameter of the methods (self) represents the current instance.
Methods are just like functions, but they can only be used through a class.

Special methods start and end with __.
Special methods have specific names:
	__init__ for the constructor
	__str__ for the conversion to string.

You can add documentation to classes, methods, and functions by using docstrings right after the definition 
	""" docstrings """

# OOO
class Elevator:
  def __init__(self, bottom, top, current):
      """Initializes the Elevator instance."""
      self.top=top
      self.bottom=bottom
      self.current=current
      pass
  def up(self):
      if self.current<self.top:
          self.current+=1 
      pass
  def down(self):
      if self.current>self.bottom:
          self.current-=1
      pass
  def go_to(self, floor):
      self.current=floor
      pass
  def __str__(self):
      return("Current floor: {}".format(self.current))

elevator = Elevator(-1, 10, 0)
elevator.up() 
elevator.current
elevator.down() 
elevator.current
elevator.go_to(10) 
elevator.current
elevator.go_to(5)
print(elevator) # __str__ definition

---
# BUILT-IN FILE OPERATIONS
open(file, mode='r')

Character | Meaning
'r' | open for reading (default)
'w' | open for writing, truncating the file first
'x' | open for exclusive creation, failing if the file already exists
'a' | open for writing, appending to the end of file if it exists
'b' | binary mode
't' | text mode (default)
'+' | open for updating (reading and writing)

f = open("test.txt") # open file in current dir, default 'r'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
f = open("test.txt", mode='r', encoding='utf-8')
f.close()

# safer, ensures file is closed properly
try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()

# or - PREFFRED !
with open("test.txt", encoding = 'utf-8') as f: # f - file variable, then whatever
		pass # or:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
    # no need to close file

f = open("test.txt",'r',encoding = 'utf-8')
f.read(4)    # read the first 4 data 'This'
f.read(4)    # read the next 4 data ' is '
f.read()  # further reading
f.tell()    # get the current file position
f.seek(0)   # bring file cursor to initial position
f.readline() # 'This is my first line\n'
f.readlines() # ['This is my first file\n', 'This file\n', 'contains three lines\n']

print(f.read())  # read the entire file from position
# or
for line in f:
    print(line, end = '')

f.write(s) # Writes the string s to the file and returns the number of characters written.

# os.* module functions
import os
os.name #name of the operating system
os.getcwd() # gets current directory and similar to "ls"
os.chdir(path)
os.pardir() # similar to ".."
os.open(path, flags, mode=511, *, dir_fd=None) 
os.chmod(path, mode, *)
os.chown(path, uid, gid, *,) #Change the owner and group id of path to the numeric uid
os.listdir()
os.environ.get("HOME", "") # get HOME variable >export HOME=asdf # to define ENV var in unix
os.environ.copy() # copy env variables

# os.path.* module
import os.path
os.path.abspath(path) #Return a normalized absolutized version of the pathname path
os.path.join(path, *paths) # return value is the concatenation of path and any members of *paths
os.path.exists(path) #Return True if path refers to an existing path or an open file descriptor
os.path.getsize(path) #Return the size, in bytes
os.path.isfile(path) #Return True if path is an existing regular file.
os.path.isdir(path) #Return True if path is an existing directory.
splitext('foo.bar.exe') # ('foo.bar', '.exe')
os.path.expanduser('~') # home directory path

# datetime.* module
import datetime
timestamp = os.path.getmtime(filename) #Return the time of last modification of path.
tm = datetime.datetime.fromtimestamp(timestamp).date()
datetime.time()
datetime.date()

# 
import socket
localhost = socket.gethostbyname('localhost') # get localhost ip
import requests
request = requests.get("http://www.google.com"); if request.status_code == 200: # check request, status, etc

# subprocess module
import subprocess
# import shlex # to break a shell command into a sequence of arguments, especially in complex cases. shlex.split(cmd_inpout_variable) 
subprocess.run(["unix_cmd", "agr1", "arg2"]) # run Unix cmd with arg >SLEEP 2
result = subprocess.run(["ls", "file_not_exists"]) # >ls file_not_exists
print (result.returncode) # returns code of error

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout) # prints STDOUT result in bytes
print(result.stdout.decode().splt()) # prints STDOUT decoded and split
print(result.stderr) # prints STDERR error out

my_env=os.environ.copy() # copy env variables

## CSV FILES
# csv read ----------------
import csv
f=open("csv_file.csv")
csv_f=csv.reader(f) # .reader function of the CSV will interpret the file as a CSV.
for row in csv_f:
	name, phone, role = row
	print("Name: {}, Role: {}, Phone: {}".format(name,role,phone))
f.close()
# csv write
hosts = [["workst.local", "192.168.1.10"], ["webserv.local", "192.168.100.100"]]
with open('hosts.csv', 'w', delimiter=',') as hosts_csv: #open with write perm.
	writer = csv.writer(hosts_csv)
	writer.writerow(hosts)

# csv dictionaries
csv.register_dialect('empDialect', skipinitialspace=True, strict=True) #The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
with open('software.csv') as software:
	reader = csv.DictReader(software) #dictreader function
	rowlist=[] #create empty list
	for row in reader:
		print (("{} has {} users").format(row["name"], row["users"])) # read keys: "name", "users" as values fr dict
		rowlist.append(row) #add to list
# csv dict writing
with open('names.csv', 'w', newline='') as csvfile:
	users = [{"first_name": "Sol", "last_name": "Mansi"},
	{"first_name": "costam", "last_name": "costam"}]
    keys = ['first_name', 'last_name'] # headers setup
    writer = csv.DictWriter(csvfile, fieldnames=keys) #if filednames not provided first row is used as keys
    writer.writeheader() # write headers
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'}) #write data row
    writer.writerows(users) #write all rows fr dictionary

# REGEX Regular Expressions
# https://www.rexegg.com/regex-quickstart.html

# The circumflex [^] and the dollar sign [$] are anchor characters. Match the start and end of a line. [^][$][.] are special characters.
re.search(r"a.e.i.", text) # r - raw string, get _first_ obj searched
re.search(r"[Pp]ython", text) # check both upper/lower Pp
re.search(r"[a-zA-Z0-9]", text) #eg. [a-z]way - any sign from  a-z;
re.search(r"[!?,.]", text) # any signs from set
re.search(r"[Aa]+.*[Aa]", text) # two occurences of A or a
r"char?acter" # one or none, can be "char?" or not -> acter, character
# . - as wildcard 1 alphanumeric sign
# ^ - start of string, 
# $ - end of string
# * - 0 or more repetitions
# + - 1 or more repetitions
# ? - 0 or 1 repetitions
# \ - escape character, use if special sign necessary as query
# [^a-z] - not included
# - - range indicator
re.search(r"\.com", text) # - exact .com phrase, \ -esacape char
re.search(r"\w*", text) # = [A-Za-z0-9_] - any alphanumeric character incl. underscore
# \w - any alphanumeric, \W - any non alphanumeric
# \s - any whitespaces, \S - any non whitespace
# \d - any decimal digit, \D - any non digit
# \b - only the whole word; r"\bword\b"
re.search(r"\w+\s+\w", text) # two groups of alphanum separated w. whitespaces (one or more)
re.search(r"^A.*a$", text) # words start "A" and end "a"
re.search(r"^[a-zA-Z_][a-zA-Z0-9_]*$", text) # valid py variable name; start with alpha, finish with alphanum, no spaces
re.search(r"^[A-Z].[a-z ].*[.?!]$", text) # sentence; starts with Upper, includes lower and space, ends with sign.
# [o+l+] - search for ol
"^[A-Za-z._-][^/@]*$" #start with ^[, [^ not include this at end
re.search(r"cat|dog", text) - OR expression, gets first

re.findall(r"...", text) # find all occurences, not first match

# REGEX Capturing Groups
result = re.search(r"^(\w*), (\w*)$", "text1, text2") # check if starts with alphanum followed by ", " and then alphanum
print(result.groups()) # groups method -> touple ('text1', 'text2'); result[0] -> text1, text2; result[1] -> text1;
re.search(r"[a-zA-Z]{5}", "a ghost") # find 5 letters - match='ghost'
re.search(r"[a-zA-Z]{5,10}", "a ghosting appeared") # find 5-10 letters
re.search(r"[a-zA-Z]{5,}", "a ghosting appeared") # find >=5 letters
re.search(r"\[(\d+)\]") # only [digits] in "[]" <- \[ this escape+"["
re.search(r"[\w.%+-]+@[\w.-]+") # email short validation

## Splitting and Replacing
re.split(r"[.?!]", text) # split sentace on given chars
re.sub(r'a', 'b', 'banana') # replace a with b -> 'bbnbnb'
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received email form asdf@gamsad.com") # replace -> Received email form [REDACTED]
re.sub(r"^([\w .-]*), ([\w .-])$", r"\2 \1", "Lovelace, Ada") # replace - starting alphanum group (\1), ending grp (\2) replace with parameters \2 \1 - changes it's place 1 to 2
re.sub(r'(?<!\S)(\d{3})-', r'(\1) ', phone) # (?<!\S) - a left-hand whitespace boundary (\d{3}) - Capturing group #1: three digits - - a hyphen.

