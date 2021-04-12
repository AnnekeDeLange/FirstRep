# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template='Hello, <name>!'):
    message_start = greeting_template[0:greeting_template.find('<')]
    message_end = greeting_template[greeting_template.find('>')+1:]
    greeting_message = f'{message_start}{name}{message_end}'
    return greeting_message

def get_gravity(body):
    gravity_solar_system_bodies = {
        'sun': 274,
        'jupiter': 24.92,
        'neptune': 11.15,
        'saturn': 10.44,
        'earth': 9.798,
        'uranus': 8.87,
        'venus': 8.87,
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62,
        'pluto': 0.58
        }
    gravity = round(gravity_solar_system_bodies[body],1)
    return gravity

def force(mass, body='earth'):
    g = get_gravity(body)
    m = mass
    force = m * g
    return force

def pull(m1: 'mass in kg', m2: 'mass in kg', d: 'distance in meters'):
    """calculates the gravitational pull between two objects (masses) given their distance"""
    gravitational_constant = 6.674*(10**-11)
    pull = gravitational_constant * (m1*m2)/d**2
    return pull


'''
print(greet('Jim'))
print(greet('Carla', "What's on your mind <name>?"))

print(force(2.0, 'mars'))
print(force(body='pluto', mass=4.167))

print(pull(800, 1500, 3))
print(pull(0.1, 5.972*10**24, 6.371*10**6))
'''