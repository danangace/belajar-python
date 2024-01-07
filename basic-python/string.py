# Using single quote or double quote

text = 'Hello World'
building = "Danang's House"

# print(text, building)

# Escaping Text
# Ingin menambahkan petik di single quote, atau di double quote

quotation_text = 'I\'m Danang'
quotation_text_2 = 'Im script "Kiddie"'
quotation_text_3 = 'Im script \"Kiddie\"'

# print(quotation_text)
# print(quotation_text_2)
# print(quotation_text_3)

# Printing multiple line in string
multiple_line = """My Name is
Danang Putra B,
I'am 8 years old
"""

# print(multiple_line)

# Escape sequence

# \n
example_text = "Danang Putra \nBahari"
# print(example_text)

# \r
example_text = "Danang Putra \rBahari"
# print(example_text)

# \t
example_text = "Danang Putra \tBahari"
# print(example_text)

# CAPITALIZE
# Return a copy of the string with its first character capitalized and the rest lowercased.
country = 'indonesia'
country.capitalize()

print(country) # Indonesia

# FIND
# Return the lowest index in the string where substring sub is found 
# within the slice s[start:end]. Optional arguments start
# and end are interpreted as in slice notation. Return -1 if sub is not found.
print(country.find('n'))

# TYPE
print(type(country))

# STRING LENGTH
print(len(country))
