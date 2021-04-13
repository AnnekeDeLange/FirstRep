# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# Modules - 1
# imports the Zen of Python

import this

# Modules 2 - time funcions - sleep()
def wait(seconds):
    """ takes seconds as a integer or float """
    from time import sleep
    sleep(seconds)
    return None

# wait(3)

# Modules 3 - sine value
def my_sin(angle):
    """ returns the sine_value of the angle. To get the sine in degrees
    use mat.sin(math.radians(x)). Maybe use a round(x,1)"""
    from math import sin
    sine_value = sin(angle)
    return sine_value

# print(my_sin(90))

# Modules 4 - ISO 8601 date time, upto minutes
def iso_now():
    from datetime import datetime
    now = datetime.today()
    my_now = now.isoformat('T', 'minutes')
    return my_now

# print(iso_now())

# Modules 5 - platform

def platform():
    import sys
    os = sys.platform
    return os

# print(platform())

# Modules 6 - greet

try:
    import greet
except ImportError:
    print('Object not found in module')


def supergreeting_wrapper(name):
    """ imports supergreeting from file greet.py in current directory """
    wrapped_supergreeting = greet.supergreeting(name)
    return wrapped_supergreeting

# print(supergreeting_wrapper("'s-Hertogenbosch"))
