#!/usr/bin/env python3

import re
import pyperclip
import pprint

# create a regex for phone number
regex = r'''
           ( ((\d\d\d)|(\(\d\d\d\())?      #code
           (\s|-)+                         #separator1
            (\d\d\d)                       #3 digit
             -                             #separator2
            (\d\d\d\d)                     #4 digits
            (((ext(\.)?\s)|x)              #extension word part
           (\d{2, 5}))?   )                #extension number part        
        '''
phone_regex = re.compile(regex, re.VERBOSE)

# create a regex for email address
regexEm = r'''
           [a-zA-Z0-9._+]+             #name part
           @                           #@ part
           [a-zA-Z0-9._+]+             #domain part part
          '''
email_regex = re.compile(regexEm, re.VERBOSE)
# Get texts off clipboard
text = pyperclip.paste()

# Extract emails and phone from the text
phone_numbers = phone_regex.findall(text)
email_addresses = email_regex.findall(text)

all_phone_numbers = []

for extracted_phones in phone_numbers:
    all_phone_numbers.append(extracted_phones[0])


# copy the extracted email/phone to the clipboard
extracted_phone_numbers = "\n".join(all_phone_numbers)
extracted_emails = "\n".join(email_addresses)
result = extracted_phone_numbers + '\n' + extracted_emails + '\n'

mmm = pyperclip.copy(result)
pprint.pprint(mmm)

