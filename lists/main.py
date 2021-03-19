# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# DEEL 1 EXERCISE
def alphabetical_order(list):
    return sorted(list, key=str.lower)
    # sorts a list of strings in alphabetical order, case insensitive

### test deel 1
# ordered_list = alphabetical_order(['Jaws', 'Star Wars: Episode IV – A New Hope', 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha'])
# print(ordered_list)                                     

# DEEL 2 EXERCISE
def list_in_lower(list,index):
    if index == int(len(list)):
        return list
    else:
        to_lower = list.pop(index)
        lowered = to_lower.lower()
        list.insert(index, lowered)
        list_in_lower(list,index+1)
        return list
###  test list_in_lower
# print(list_in_lower(['Jaws', 'Star Wars: Episode IV – A New Hope', E.T. the Extra-Terrestrial', 'Memoirs of a Geisha'],0))

def won_golden_globe(film_name):
    films_with_golden_globes = ['Jaws', 'Star Wars: Episode IV – A New Hope', 
                                'E.T. the Extra-Terrestrial',
                                'Memoirs of a Geisha']
    if film_name in films_with_golden_globes: 
        return True
    elif film_name.lower() in list_in_lower(films_with_golden_globes,0):
        return True
    else: return False
### test deel 2
# print(won_golden_globe('star wars: Episode IV – A New Hope'))


# DEEL 3 EXERCISE
def remove_toto_albums(mixed_up_list):
    toto_list = ['Fahrenheit', 'The Seventh One',
                 'Toto XX (two previously unreleased songs)',
                 'Falling in Between (sharing lead vocals on one song)',
                 '35th Anniversary – Live in Poland',
                 'Toto XIV', 'Old Is New',
                 '40 Tours Around the Sun - Live in Holland']
    print(toto_list)
    print(mixed_up_list)
    if 'Fahrenheit' in mixed_up_list:
        mixed_up_list.remove('Fahrenheit')
    if 'The Seventh One' in mixed_up_list:
        mixed_up_list.remove('The Seventh One')
    if  'Toto XX (two previously unreleased songs)' in mixed_up_list:
        mixed_up_list.remove('Toto XX (two previously unreleased songs)')
    if  'Falling in Between (sharing lead vocals on one song)' in mixed_up_list:
        mixed_up_list.remove('Falling in Between (sharing lead vocals on one song)')
    if  '35th Anniversary – Live in Poland' in mixed_up_list:
        mixed_up_list.remove('35th Anniversary – Live in Poland')
    if  'Toto XIV' in mixed_up_list:
        mixed_up_list.remove('Toto XIV')
    if  'Old Is New' in mixed_up_list:
        mixed_up_list.remove('Old Is New')
    if  '40 Tours Around the Sun - Live in Holland' in mixed_up_list:
        mixed_up_list.remove('40 Tours Around the Sun - Live in Holland')
    return mixed_up_list

'''
### test deel 3
test_list = ['Fahrenheit', 'The Seventh One',
                 'Toto XX (two previously unreleased songs)',
                 'Falling in Between (sharing lead vocals on one song)',
                 'Toto XIV', 'Old Is New',
                 '40 Tours Around the Sun - Live in Holland','Jaws',
                 '35th Anniversary – Live in Poland',
                 'Star Wars: Episode IV – A New Hope',
                 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']

print(remove_toto_albums(test_list))    # test remove_toto_albums(x)
'''
