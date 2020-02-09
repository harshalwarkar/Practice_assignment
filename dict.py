a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}

a['dougnut'] = 'sarkar'

print(a)
print(a['apple'])

b = {'school': 'dks', 'new': 'one', 'ls': [1, 2, 3.5]}
print(b)
print(b['ls'])

# to print the parameter from list of dictionary
print(b['ls'][2])

# to update the dictionary
b['school'] = 'symbosis'
print(b)

# to get all keys of dictionary
print(b.keys())

# We can also access each key-value pair within a dictionary using the items() method:
print(b.items())


