# String : an ordered sequence of characters
# string is immutable
name='Amir'
print(type(name))
print(len(name)) # empty spaces are also counted
# indexing : every element of string is stored on specific index starts from zero
word='programming'
print(word[0]) # p
print(word[3]) # g
print(word[-1]) # it will return last element
print(word[-3]) # i
# Slicing : Extracting specific portion from a string. syntax str[start:end:step]
field='networking'
print(field[0:3]) # net because the 3 excluded
print(field[:7]) # network
print(field[-7:-1]) # workin
print(field[0::2]) # it will skip one element ntokn

# Operator on string
first_name='Amir '
last_name='Bacha'
full_name=first_name+last_name # + sign is used for concatenation (Joinin) of string
print(full_name)
print(first_name*3)
print('i' in first_name) # True

# Built in function on string
# Case conversion
statement='I am learning python'
print(statement.upper())
print(statement.lower())
print(statement.capitalize())
print(statement.title())
print(statement)
name=' AmIr '
print(name.swapcase())

print(name.strip())
print(name.lstrip())
print(name.rstrip())
print(name)
name=name.lstrip()
print(name)
field = 'Programming'
print(field.find('b')) # on the other hand the index will give us error
print(field.count('r'))

fav_fruit='My favourate fruit is mango'
fav_fruit=fav_fruit.replace('mango','banana')
print(fav_fruit)
name='Amir bacha '
age=22
print(f"my name is {name} and i am {age} years old")
print('my name is {} and i am {} years old '.format(name,age))

# Splitting: Dividing the string into substrings using seperator
languages='c++ java python js'
print(languages.split())
opinion='we  should stay here'
print(opinion.split(' ',2))
