
def test_print(a, b, c, d):
    print(a, b, c, d)


test_print("Yogesh", "Suresh", "Mahesh", "Ajay")
# ----------------------------------------------------------

# to implement scalable application to add billions of users this approach is not good.
# so if we add names in one list and will pass that list also if list change then also it works
# it goes as a tupple


def test_args(*args):
    print(args[0:3])


har = ["Yogesh", "Suresh", "Mahesh", "Ajay"]

test_args(*har)
# ----------------------------------------------------------
# We are also able to run the for loop

def data_args(*args):
    for i in args:
        print(i)

har = ["Yogesh", "Suresh", "Mahesh", "Ajay"]

data_args(*har)
# ----------------------------------------------------------
# We are also able add normal argument with it. Always normal arguments come first and then *args

def proj_args(normal, *args):
  print(*args)
  print(normal)


har = ["Yogesh", "Suresh", "Mahesh", "Ajay"]
normal = "I am a noraml argument"

proj_args(normal, *har)
# ----------------------------------------------------------
def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


my_dict = {"name": "Paresh", "Age": 19, "surname": "Patil"}

test_kwargs(**my_dict)
# ----------------------------------------------------------

def proj_argskw(normal, *args, **kwargs):
    print(*args)
    print(normal)
    for key, value in kwargs.items():
        print(key, value)


dict_one = {"name": "Paresh", "Age": 19, "surname": "Patil"}
har = ["Yogesh", "Suresh", "Mahesh", "Ajay"]
normal = "I am a noraml argument"

proj_argskw(normal, *har, **dict_one)


