# Python Types Intro
# Motivation:

def get_full_name(firstname, lastname):
    fullname = firstname.title() + ' ' + lastname.title()
    return fullname

print(get_full_name('ahmed','ali'))

#Add Types
# Let's modify a single line from the previous version.

# We will change exactly this fragment, the parameters of the function, from:

def get_full_name(firstname:str, lastname:str):
    fullname = firstname.title() + ' ' + lastname.title()
    return fullname

print(get_full_name('kamran','akmal'))

# More motivation

def get_name_with_age(name:str, age:int):
    name_with_age = name + " is this old: " + str(age)  #Now you know that you have to fix it,
    return name_with_age                              # convert age to a string with str(age):

print(get_name_with_age('Akmal',34))

#Declaring types:
'''You can declare all the standard Python types, not only str.
You can use, for example:
int
float
bool
bytes'''

def get_items(item_a:str, item_b:int, item_c:float, item_d:bool, item_e: bytes):
    return item_a, item_b, item_c, item_d,item_e

#Generic types with type parameters

# List:
# For example, let's define a variable to be a list of str.
def proess_items(items: list[str]):
    for item in items:
        print(item)

'''
Those internal types in the square brackets are called "type parameters".
In this case, str is the type parameter passed to List (or list in Python 3.9 and above).
'''
# Tuple and Set
# You would do the same to declare tuples and sets

def process_items(items_t:tuple[int,int,str], items_s: set[str]):
    return items_s, items_t

# Dict
'''
To define a dict, you pass 2 type parameters, separated by commas.
The first type parameter is for the keys of the dict.
The second type parameter is for the values of the dict:
'''

def process_items(prices: dict[str,int]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# Union
'''
You can declare that a variable can be any of several types, for example, an int or a str.
In Python 3.6 and above (including Python 3.10) you can use the Union type from typing and put inside the square brackets the possible types to accept.
In Python 3.10 there's also a new syntax where you can put the possible types separated by a vertical bar (|).
'''
def process_items(item: str | int):
    print(item)

# Possibly None
'''
You can declare that a value could have a type, like str, but that it could also be None.
In Python 3.6 and above (including Python 3.10) you can declare it by importing and using Optional from the typing module.
'''

from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"{name}")
    else:
        print("Hello world!")

print(say_hi())

'''
Using Optional[str] instead of just str will let the editor help you detecting errors where you could be assuming that a value is always a str, when it could actually be None too.
Optional[Something] is actually a shortcut for Union[Something, None], they are equivalent.
'''
def say_hi(name: str | None = None):
    if name is not None:
        print(f"{name}")
    else:
        print("Hello World!!!")

print(say_hi())

# Using Union or Optional
'''
If you are using a Python version below 3.10, here's a tip from my very subjective point of view:
🚨 Avoid using Optional[SomeType]
Instead ✨ use Union[SomeType, None] ✨.
Both are equivalent and underneath they are the same, but I would recommend Union instead of Optional because the word "optional" would seem to imply that the value is optional, and it actually means "it can be None", even if it's not optional and is still required.
I think Union[SomeType, None] is more explicit about what it means.
It's just about the words and names. But those words can affect how you and your teammates think about the code.
'''

from typing import Optional

def say_hi(name: Optional[str]):
    print(f"Hey {name}!")

# say_hi()  #it throws an error because we don't pass parameter in it

say_hi(name=None)   # This works, None is valid

def say_hi(name: str | None):
    print(f"Hey {name}!")

#Generic types
'''
These types that take type parameters in square brackets are called Generic types or Generics, for example:
You can use the same builtin types as generics (with square brackets and types inside):

list
tuple
set
dict
And the same as with Python 3.8, from the typing module:

Union
Optional (the same as with Python 3.8)
...and others.
'''

# Classes as types
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

'''
Notice that this means "one_person is an instance of the class Person".
It doesn't mean "one_person is the class called Person".
'''

# Pydantic models
'''
Pydantic is a Python library to perform data validation.
You declare the "shape" of the data as classes with attributes.
And each attribute has a type.
Then you create an instance of that class with some values and it will validate the values, convert them to the appropriate type (if that's the case) and give you an object with all the data.
And you get all the editor support with that resulting object.
'''
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": '24',
    "name": "John Doe",
     "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"]
}
user = User(**external_data)
print(user)
print(user.id)
print(user.name)

# Type Hints with Metadata Annotations
# Python also has a feature that allows putting additional metadata in these type hints using Annotated.

from typing import Annotated

from typing import Annotated


def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"

# Type hints in FastAPI
'''
FastAPI takes advantage of these type hints to do several things.

With FastAPI you declare parameters with type hints and you get:

Editor support.
Type checks.
...and FastAPI uses the same declarations to:

Define requirements: from request path parameters, query parameters, headers, bodies, dependencies, etc.
Convert data: from the request to the required type.
Validate data: coming from each request:
Generating automatic errors returned to the client when the data is invalid.
Document the API using OpenAPI:
which is then used by the automatic interactive documentation user interfaces.

The important thing is that by using standard Python types, in a single place (instead of adding more classes, decorators, etc), FastAPI will do a lot of the work for you.


'''