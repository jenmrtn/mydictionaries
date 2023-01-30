person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
print(person.get('children')[1])
print(person['children'][1])
print(person['pets']["cat"])

for i in person["children"]:
    print(i) #i is a string

for i, j in person['pets'].items:
    print(f"Type of pet:{i} name of pet: {j}")
#Splits kets and values up