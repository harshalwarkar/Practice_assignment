# Write a Python program to sort (ascending and descending) a dictionary by value.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original list: ", d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ', sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
# -------------------------------------------------------------------------------
# to add a key to a dictionary.
k = {1: 10, 2: 20, 3: 30}
k.update({4: 40})
print(k)
# -------------------------------------------------------------------------------
# program to concatenate following dictionaries to create a new one.
s = {'ajay': 'amar'}
s1 = {'ramesh': 'suresh'}
s2 = {'Krisha': 'sudesh'}
s3 = {}
for i in s, s1, s2:
    s3.update(i)
print(s3)
# -------------------------------------------------------------------------------
#  Python program to check whether a given key already exists in a dictionary.


def checkdict(x):
    a1 = {1: 10, 5: 50, 6: 60}
    if x in a1:
        print("key is available in dictionary")
    else:
        print("key is not available dictionary")


checkdict(5)
# -------------------------------------------------------------------------------
# Write a Python program to iterate over dictionaries using for loops.
a2 = {"ajay": "atul", "ganesh": "mahesh", "sunil": "pravin"}
for i in a2:
 # print(i)
 print(a2[i])





