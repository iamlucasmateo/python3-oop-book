# Named tuples: useful when you need grouped data, you want to name it
# (better readability than a tuple), you don't need behaviour (so that
# an object doesn't make sense) and you will not modify it (in which case you
# would use a dictionary instead)
from collections import namedtuple

# edificio de los pabellones
Building = namedtuple("Building", "numero calle altura")
my_building = Building(28, "Ezeiza", 2787)

print("access named attribute")
print(my_building.calle)

print("\ntuple unpacking")
numero, calle, altura = my_building
print(calle)

print("\nassignment (forbidden)")
try:
    my_building.numero = 100
except Exception as e:
    print("exception raised")
    print(e)


# Dictionaries: different types of keys
my_dict = dict()

my_dict["string_key"] = "a string as key"
my_dict[1] = "also an integer as key"
my_dict[12.5] = "float as key"
my_dict[("a", "tuple",)] = "you can use tuples too"

class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue
my_dict[AnObject("value")] = "object as key"

print("Dictionaries: different types of keys")
for i, (k, v) in enumerate(my_dict.items()):
    print("\n", i, type(k))
    print(my_dict[k])


# Mutable types are not hashable
example_list = [1,2,3]

try:
    my_dict[example_list] = "list as key"
except Exception as e:
    print("lists cannot be keys", e)


example_dict = { "key1": "value1", "key2": "value2" }

try:
    my_dict[example_dict] = "dict as key"
except Exception as e:
    print("dicts cannot be keys", e)


# useful alternatives
from collections import defaultdict

print("")
print("defaultdict")
my_dict = defaultdict(int)
print("int as default", my_dict["a_key"])

my_dict = defaultdict(list)
print("list as default", my_dict["a_key"])


# counter
from collections import Counter
import random

choices = ["apple", "banana", "peach", "orange", "cherry", "pear", "chocolate"]
my_list = [ random.choice(choices) for i in range(50) ]
counter = Counter(my_list)
print("")
print("Counter data structure")
print("access key cherry:", counter["cherry"])
print(counter.most_common())
print(counter.most_common(3))

# Lists
# sorting lists
from operator import itemgetter 
# others used from operator: methodcalled, attrgetter
my_list = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
print("")
print("Sortings lists")
print("sorting tuples by first element (default)")
my_list.sort()
print(my_list)
print("\nsorting tuples by second element (using key)")
my_list.sort(key=itemgetter(1))
print(my_list)

# Sets: most useful when we use more than one
# add, union, intersection, difference, symmetric_difference