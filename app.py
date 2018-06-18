# This code will use Regular Expressions to scan through strings, so the first step is to import the appropriate module!

import re

phone_pattern = re.compile(r'''(\d{3}|\(\d{3}\)) # This is for the area code, with and without parentheses. The pipe '|' is used to look for either combination, where '\d' looks for numbers,specifically '{3}'. It is important to note that we need escape characters for the parentheses because regex will recognize it as another group otherwise.
(\s|-|\.)* # This looks for either a space, dash, or period. The asterisk '*' looks for '0 or more' of the preceding group. So, in the case that a number is printed without spaces or a special character, the program will still find the number. It is important to note the period '.\' needs an escape backslash because regex will look at it as a wildcard character otherwise.
(\d{3}) # Here we have the next (3) numbers.
(\s|-|\.)* # Here is the next space, dash, or period.
(\d{4})
''', re.VERBOSE) # 'VERBOSE' allows for the use comments in regex.


email_pattern = re.compile(r'''[a-zA-Z0-9._-]+ # A new class was created to only look for letters, numbers, and some common email symbols. The '+' symbol means '1 or more' characters, since we need at least (1) character to create an email address.
@ # This is simply the '@' symbol
[a-zA-Z0-9._-]+ # This is for the domain name.
\. # Here is the escaped '.' character.
[a-zA-Z0-9]+''' # This is for the top-level domain name, e.g. '.com', '.edu'.
, re.VERBOSE) # It is important to note that this pattern does not have groups because a regex method called 'findall' does not work well with them. 


some_string = '''angel33@gmail.com 
csjkcsa c 8182329081 (804)2374085
(800) 377 8180 \n
\n(808) 207 1086
223-808-1233 129.293.3232
jflerres@yahoo.com''' # We will test this string.

