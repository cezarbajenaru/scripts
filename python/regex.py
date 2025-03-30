# you can actually print the pattern and attach different methods to it like .groups() in this case to create a touple
import re
result = re.search(r"^(\w*), (\w*)$", "Lovalace, Ada")
print(result) #prints the match object
print(result.groups()) #prints all captured groups as a tuple
print(result[0]) # prints the entire matched string
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))


import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return print("{} {}".format(result[2], result[1]))
rearrange_name("Lovalace, Ada")


import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return print("{} {}".format(result[2], result[1]))
rearrange_name("Ritchie, Dennis")

import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return print("{} {}".format(result[2], result[1]))
rearrange_name("Hopper, Grace M.")

# repetition qualifiers bellow

import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
#the first 5 character word will be found

import re
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
#the first 5 character word will be found, but there are more

import re
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
#using findall will give you all the 5 character results

import re
print(re.findall("\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
#finds all characters that have five characters or more and prints only
#['scary', 'ghost', 'appea']

import re
print(re.findall(r"\w{5,}", "I really like strawberries"))
#the words that have 5 or more characters will be printed

import re
print(re.search(r"s\w{,20}", "I really like strawberries"))


extracting PID bellow ( process ID)
import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
print(result[1]) #cannot match because there are no digits

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
#bellow log_line will take "log" variable values. log_line exists so it can be put inside "result="
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))


import re
re.split(r"[.?!]", "One sentence. Another one? And the last one!")
#splits at the matching characters
#the split delimiter is chosen to be .?!
#Will return a list of strings ( not because of the square brackets) Square brackets mean characted set to be matched

import re
re.split(r"([.?!])", "One sentence. Two Sentences? And the last one!")
#splits at the matching caracters
#will return a list of strings but with the delimiters included. () capturing parenthesis prints everything
#will output a final empty string because the string ends with a delimiter and creates by default an empty string

import re
printer = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "received an email for go_nuts95@my.example.com")
print(printer)
#substitutes the \1 string into \2 placeholder string
#first it matches the text that resembles an email and then substitutes it with, let's say, a variable


import re
re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
#(r"\2 \1") is a reorder group. Placeholder strarts from 1 ( 0 is the whole string ) and reorders placeholders

#>>> re.sub(r”([A-Z])\.\s+(\w+)”, r”Ms. \2”, “A. Weber and B. Bellmas have joined the team.”)
# for example above, the first argument is the string that we look for and capture, the second is what to substitute and third is the string to be modified
#re.sub(pattern, replacement, string)

import re
def transform_record(record):
    new_record(re.sub(r""))

import re
pattern = r"\w+\s\w+),(\d+-\d+-\d+,),(\w*)"
text = "Sabrina Green,802-867-5309,System Administrator"
match = re.search(pattern, text)
print(match)

import re
def transform_record(record):
  new_record = re.sub(r"(\w+\s\w+),(\d+-\d{3}-\d+),(\w*)", r"\1,(+1-\2),\3", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer


  new_record = re.sub(r"(\w+\s\w+),(\d+-\d{3}-\d+),(\w*)", r"\1,+1-\2,\3", record)

  pattern = r"(\b\w*[aeiouAEIOU]{3,}\w*\b)"

  result = re.sub(r"#+", r"//", line_of_code)

  result = re.sub(r"(\b\d{3})-(\d{3})-(\d{4}\b)", r"(\1) \2-\3", phone)

import re
def parse_city_country(text):
  pattern = r"([A-Za-z\s]+),\s([A-Za-z]+)"
  result = re.search(pattern, text) #enter the re method  here
  if len(result) != 2:
    return ""
  return result.group(1), result.group(2) #return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank
