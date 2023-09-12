## first Qwiklabs Assessment: Working with Python Scripts

#!/usr/bin/env python3
# above is *hash bang* or shebang
from network import *
import shutil
# shutil module offers a number of high-level operations on files and collections of files. In particular, it provides functions that support file copying and removal. It comes under Python's standard utility modules. disk_usage() method is used to get disk usage statistics of the given path. This method returns a named tuple with the attributes total, used, and free.
import psutil
# psutil (Python system and process utilities) is a cross-platform library for retrieving information on the processes currently running and system utilization (CPU, memory, disks, network, sensors) in Python. It's useful mainly for system monitoring, profiling, limiting process resources, and managing running processes. cpu_percent() returns a float showing the current system-wide CPU use as a percentage.
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk > 20%"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
# not enough - print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")



# wk2
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
for i in initial_guests:
    guests.write(i + "\n")
guests.close()

new_guests = ["Sam", "Danielle", "Jacob"]
with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")
guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]
with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())
with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

guests_to_check = ['Bob', 'Andrea']
checked_in = []
with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

# 
import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")

# ASSIGNMENT for CSV ---
##The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 
import os
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.makedirs(directory, exist_ok=True)
  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename,"w") as file:
    pass
  os.chdir("..")
  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))

# read CSV file
import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()
# write rows CSV file
import csv
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

# read csv to Dictionary - DictReader CSV file
import csv
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))

# csv write dictionary
import csv
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
          {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
          {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    # following line will create the heading in the csv file
    writer.writeheader()
    writer.writerows(users)

# csv to sql ---
import sqlite3
def csv_sql(file_dir,table_name,database_name):
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS %s;" % table_name) # Drop the current table by this line
    with open(file_dir, 'r') as fl:
        hd = fl.readline()[:-1].split(',')
        ro = fl.readlines()
        db = [tuple(ro[i][:-1].split(',')) for i in range(len(ro))]

    header = ','.join(hd)
    cur.execute("CREATE TABLE IF NOT EXISTS %s (%s);" % (table_name,header))
    cur.executemany("INSERT INTO %s (%s) VALUES (%s);" % (table_name,header,('?,'*len(hd))[:-1]), db)
    con.commit()
    con.close()

csv_sql('./employees.csv','tableName','employees.db')

# 
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 
  relative_parent = os.path.join(os.getcwd(), os.pardir)
  # print(relative_parent)
  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)
print(parent_directory())

# 
import os
import datetime
def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w+") as file:
    pass
  timestamp=os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  time=datetime.datetime.fromtimestamp(timestamp).date()
  # Return just the date portion yyyy-mm-dd -> [:10]
  return ("{}".format(str(time)[:10]))

print(file_date("newfile.txt")) # today's date in the format of yyyy-mm-dd

# wk1 assignment 1 - health_checks.py
#!/usr/bin/env python3
import shutil
import psutil
from network import *
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("ERROR")

# wk1 assignment 1 - network.py module
import requests 
import socket 
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        return True
    else:
        return False
    # return localhost == '127.0.0.1' #alternative

def check_connectivity():
    request = requests.get("http://www.google.com")
    if request.status_code == 200:
        return True
    else:
        return False
    # return request.ok #alternative

# CSV files
import os
import csv
# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")
# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""
  create_file(filename)   # Call the function to create the file 
  with open(filename) as dictiofile:   # Open the file
    reader=csv.DictReader(dictiofile)    # Read the rows of the file into a dictionary
  for row in reader:    # Process each item of the dictionary
    return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

print(contents_of_file("flowers.csv")) #Call the function

#
import os
import csv
# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")
# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""
  create_file(filename) # Call the function to create the file 
  f=open(filename)  # Open the file
  rows = csv.reader(f)    # Read the rows of the file
  next(rows)
  for row in rows:    # Process each row
    name,color,type = row
    return_string += "a {} {} is {}\n".format(color,name,type)
  f.close()    # Format the return string for data rows only
  return return_string
print(contents_of_file("flowers.csv")) #Call the function

# wk2 assignment generate_report.py
#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list
def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list): #This uses the set() method, which convert$
                department_data[department_name] = department_list.count(department_name)
        return department_data
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

employee_list = read_employees('/home/student-02-efd653a4a086/data/employees.csv')
#print(employee_list)
dictionary = process_data(employee_list)
print(dictionary)
write_report(dictionary, '/home/student-02-efd653a4a086/test_report.txt')

# REGULAR EXPRESSIONS ---
## re module - wk#3
import re
def check_aei (text):
  result = re.search(r"a.e.i.", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

## Practice Quiz: Basic Regular Expressions
### ass checks if proper web address
import re
def check_web_address(text):
  pattern = "^[A-Za-z._-][^/@]*$" #start with, [^ not include this at end
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

### correct time format
import re
def check_time(text):
  pattern = "[1-9][0-2]?:[0-5][0-9] ?[aApM][mM]" #proper time format
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

### zip code
import re
def check_zip_code (text):
  result = re.search(r".\d{5}(?:-\d{4})?", text)
  #result = re.search(r"\d{5}(?:-\d{4})?", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

## Rearrange name
import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w .-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
print(rearrange_name("Kennedy, John F."))

## Extracting a PID Using regexes in Python
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]\: ([A-Z]+)" # search for [digits] & UPPER
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


#wk3 Practice Quiz: Advanced Regular Expressions
##1.Question 1. We're working with a CSV file, which contains employee information. Each record has a name field, followed by a phone number field, and a role field. The phone number field contains U.S. phone numbers, and needs to be modified to the international format, with "+1-" in front of the phone number. Fill in the regular expression, using groups, to use the transform_record function to do that.
import re
def transform_record(record):
  new_record = re.sub(r",([\d-]+)",r",+1-\1" ,record)
  return new_record
print(transform_record("Sabrina Green,802-867-5309,System Administrator")) # Sabrina Green,+1-802-867-5309,System Administrator
print(transform_record("Eli Jones,684-3481127,IT specialist")) # Eli Jones,+1-684-3481127,IT specialist
print(transform_record("Melody Daniels,846-687-7436,Programmer")) # Melody Daniels,+1-846-687-7436,Programmer
print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) # Charlie Rivera,+1-698-746-3357,Web Developer

# 2. Question 2. The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.
import re
def multi_vowel_words(text):
  pattern = r"\b[A-Za-z]*[aeiou]{3,}[A-Za-z]*\b"
  result = re.findall(pattern, text)
  return result
print(multi_vowel_words("Life is beautiful")) # ['beautiful']
print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) # ['Obviously', 'queen', 'courageous', 'gracious']
print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) # ['rambunctious', 'quietly', 'delicious']
print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) # ['queue']
print(multi_vowel_words("Hello world!")) # []

# 4. Question 4. The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 
import re
def transform_comments(line_of_code):
  result = re.sub(r"#+",r"//",line_of_code) # find: 1+ of "#", replace: "//"
  return result
print(transform_comments("### Start of program")) # Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) # Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) # Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) # Should be "  return(number)"

# 5. Question 5. The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.
import re
def convert_phone_number(phone):
  result = re.sub(r'(?<!\S)(\d{3})-(\d{3})-(\d{4}\b)', r'(\1) \2-\3', phone)
  return result
print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300


#wk3 ASSIGNMENT
#!/usr/bin/env python3
import re
import csv
def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False
def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '/home/student-02-efd653a4a086/data/user_email.csv' #<csv_file_location>
  report_file = '/home/student-02-efd653a4a086/data' + '/updated_user_emails.csv' #<path_to_home_directory>
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()
main()

##wk 4 - Managing Data and Processes
export NEWENVVAR = asdf # unix new env variable
import sys
sys.argv # argv stores CLI arguments
echo $? # exit code value=0 if no error in UNIX
sys.exit(1) # defines exit code 1 for error in py

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

#wk4.3 - Filtering Log Files with Regular Expressions
import re
def show_time_of_pid(line):
  pattern = r'^(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+) [\w\.]+ [\w=]+\[([0-9]+)\]'
  pattern = r"(\w+ \d+ \d+:\d+:\d+)+.*?\[(\d+)\]"

  result = re.search(pattern, line)
  return f'{result[1]} pid:{result[2]}'
print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

# starting dictionary
usernames={}
name='user1'
usernames[name]=usernames.get(name,0)+1 # when no name as key in usernames, value is 0, when key is present -> +1
print(usernames)

#wk4.4 - Working with Log Files
#!/usr/bin/env python3
import sys
import os
import re
def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)

> ./find_error.py ~/data/fishy.log

# persistence and determination
# Hejka tato, widze ze sie uczysz trzymaj tak dalej a bedziesz najlepszy GAJA
