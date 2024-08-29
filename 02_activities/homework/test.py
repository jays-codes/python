def is_416_number(number):
    '''Check wether the number has 416 area code'''
    #number should be not less than 10 characters
    if len(number) < 10:
        return False    
    #check if the number variable has 416 area code
    if '416' in number:
        return True
    else:
        return False

print(is_416_number('416-555-5555'))
print(is_416_number('647-555-5555'))
print(is_416_number('4165551234'))

# function without a parameter
def jays_tester():
    str = "jay"
    print("\t"+str)

jays_tester()

def isPalindrome(str):
    return str==str[::-1]

print(isPalindrome("saias"))

str = "alphabet"
has = 'a' in str
print()

import re
match = re.search('a', str)
print(match)

#use regex to check a phone number
import re

def is_valid_phone_number(phone_number):
    pattern = r'^[2-9]\d{2}-\d{3}-\d{4}$'
    return re.match(pattern, phone_number) is not None

print(is_valid_phone_number('416-555-5555'))  # Should return True
print(is_valid_phone_number('647-555-5555'))  # Should return False

#use regex to check if phone number has the area code 416
import re
def has_416_area_code(phone_number):
    pattern = r'^416-\d{3}-\d{4}$'
    return re.match(pattern, phone_number) is not None

print(has_416_area_code('416-555-5555'))  # Should return True
print(has_416_area_code('647-416-5555'))  # Should return False

