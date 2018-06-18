# This code will use Regular Expressions to scan through strings, so the first step is to import the appropriate module!

import re

phone_pattern = re.compile(r'''(\d{3}|\(\d{3}\)) # This is for the area code, with and without parentheses. The pipe '|' is used to look for either combination, where '\d' looks for numbers,specifically '{3}'. It is important to note that we need escape characters for the parentheses because regex will recognize it as another group otherwise.
(\s|-|\.)* # This looks for either a space, dash, or period. The asterisk '*' looks for '0 or more' of the preceding group. So, in the case that a number is printed without spaces or a special character, the program will still find the number. It is important to note the period '.\' needs an escape backslash because regex will look at it as a wildcard character otherwise.
(\d{3}) # Here we have the next (3) numbers.
(\s|-|\.)* # Here is the next space, dash, or period.
(\d{4})
)''', re.VERBOSE)

