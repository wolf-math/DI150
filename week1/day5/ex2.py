# Delete set of keys from Python Dictionary


person = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]

for key in list(person.keys()):
    if key in keys_to_remove:
        del person[key]

print(person)