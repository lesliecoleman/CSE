# Dictionaries - Made up of key: value pair

dictionary = {"name": 'Jeffery', 'age': 1, 'height': 100 * 12 + 11}

# Accessing things from a dictionary
print(dictionary['name'])
print(dictionary['height'])
print(dictionary['age'])

large_dictionary = {
    'CA': 'California',
    'AZ': 'Arizona',
    'NY': 'New York'
}

print(large_dictionary['NY'])

larger_dictionary = {
    'CA': [
        'Fresno',
        'San Francisco'
        "San Jose"
    ],
    'AZ': [
        'Phoenix',
        'Tuscon'
    ],
    'NY': [
        'New York City',
        'Brooklyn'
    ]
}
print(larger_dictionary['NY'])
print(larger_dictionary['NY'][1])