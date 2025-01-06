import json

with open('file.json', 'r') as file_obj:
    my_family = json.load(file_obj)


my_family['children'][0]['favoriteColor'] = 'Ebony'
my_family['children'][1]['favoriteColor'] = 'Dark Black'

print(my_family)

with open('file.json', 'w') as file_obj:
    json.dump(my_family, file_obj, indent = 2, sort_keys=True)
