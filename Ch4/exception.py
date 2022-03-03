# classes inheriting from BaseException: 
# SystemExit, KeyboardInterrupt and Exception

# dealing with different types of exceptions

def funny_division2(anumber):
       try:
           if anumber == 13:
               raise ValueError("13 is an unlucky number")
           return 100 / anumber
       except (ZeroDivisionError, TypeError):
           return "Enter a number other than zero"


def funny_division3(anumber):
       try:
           if anumber == 13:
               raise ValueError("13 is an unlucky number")
           return 100 / anumber
       except ZeroDivisionError:
           return "Enter a number other than zero"
       except TypeError:
           return "Enter a numerical value"
       except ValueError:
           print("No, No, not 13!")
           raise

# else, finally

import random
some_exceptions = [ValueError, TypeError, IndexError, None]
try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" %
        ( e.__class__.__name__))
else:
       print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")


