import re

'''
This program opens a file, reads each line, 
matches the regular expression pattern of an IP address, 
and outputs the result to the command line.

note: The file that is desired to be parsed must be located 
in the same directory as ip_address_parser.py program.  
''' 

#function that removes duplicates
def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

#file_name is text file that is being parsed for ip addresses
file_name = input("Enter the exact log file name (include the file extension): ")

#This is an empty list that later contain all of the discovered IP addresses. It is used to remove the initial duplicated IPs. 
no_duplicate = []

#Regex pattern for IP address pattern
ip_pattern = re.compile(r"(?P<ipv4>(?<![0-9])(?:(?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})[.](?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})[.](?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})[.](?:25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2}))(?![0-9]))")

with open(file_name, 'r') as f:
    lines = f.readlines()
    #print(lines)

    for line in lines: 
        match = re.search(ip_pattern, line)
        if match:
         # Make sure to add \n to display correctly when we write it back
            new_line = match.group()
        #new_file.append(new_line)
            no_duplicate.append(new_line)

#opens log file and reads its contents line by line
with open(file_name, 'r') as f:
    lines = f.readlines()

#iterates through the opened file and matches the regex IP address pattern 
    for line in lines: 
        match = re.search(ip_pattern_next, line)
        if match:
            new_line = match.group()
            no_duplicate.append(new_line)
        
#more removing of duplication 
new_list = []
for i in no_duplicate:
    if i not in new_list:
        new_list.append(i)

#take out all of the /n (this is specific to a log file I tested but replace() can be used to remove any additional characters) 
new_list_2 = []
for n in new_list: 
    new_list_2.append(n.replace("\n", ""))

#remove duplicates with remove_dup function
remove_dup(new_list_2)
print(new_list_2)
    
