# empty dictionary
s = {}

# Dictionary with Integer key
s1 = {1: "Harshal", 2: "Vaibhav"}

# Dictionary with String key
s2 = {"Fruit": "apple", "Fruit1": "Banana"}

# Dictionary with list and tupple in it
s3 = {"one": [1, 2, 3, 4], "fruit": ("A", "b")}
s4 = {"two": [1, 2, {"bird": "Parrot"}, 3]}

# using dict
my_dict = dict({"fruit": 1, "bird": 2})
print(my_dict)
# -----------------------------------------------------
# Access elements from dictionary

s5 = {"name": "Jack", "Age": 21, 1: "Run"}
print(s5["name"])
print(s5["Age"])
print(s5[1])

s3 = {"one": [60, 78, 21, 90], "fruit": ("A", "b")}
print(s3["one"][1])
print(s3["fruit"][0])

s4 = {"two": [70, 31, {"bird": "Parrot", "age": 16}, 3]}
print(s4["two"][2]["bird"])
print(s4["two"][2]["age"])
# ---------------------------------------------------------
# Change elements in a dictionary
s6 = {"name": "Nick", "age": 21}
s6["name"] = "Nill"
print(s6)
s7 = {"two": [70, 31, {"bird": "Parrot", "age": 16}, 3]}
s7["two"][2]["bird"] = "Parrot_one"
print(s7)
# ---------------------------------------------------------
# Add elements in a dictionary
s8 = {"two": [70, 31, {"bird": "Parrot", "age": 16}, 3]}
s8["Surname"] = "Patil"
print(s8)
# ---------------------------------------------------------
# remove a particular item
s9 = {"car": ["wagonr", {"bike": "Pulsar", "bike2": "Passion"}, "Suzuki"]}
print(s9.pop(1))




