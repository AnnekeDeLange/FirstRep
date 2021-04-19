# Do not modify these lines
import os

__winc_id__ = '534d85ea1ab14924a91f9eccf6f3f30d'
__human_name__ = 'errors'


# Test your functions here to make sure the functionality remains the same.
def main():
    # foo = list(range(10))
    # print(get_item_from_list(foo, 9),
    #       get_item_from_list(foo, -1),
    #       get_item_from_list(foo, 10))
    ### testing lines for changing add() to add_eafp
    # print(add_lbyl('aha', 'john'))
    # print(add_lbyl('aha', 'john'))
    # print(add_lbyl('aha', 8))
    # print(add('aha', 8))
    # print(add_lbyl('aha', 3.5))
    # print(add('aha', 3.5))
    # print(add_lbyl(['aha'], 3))
    # print(add(['aha'], 3))
    ### testing lines for changing readfile() to add_eafp
    # print(read_file_lbyl("C:/Users/Anneke/testfile.txt"))
    # print(read_file("C:/Users/Anneke/pestfile.txt"))
    ### testing lines for changing readfile() to add_eafp
    # testlist = list('abcde')
    # testlist2 = ['e', 1, 2, "een stukje tekst"]
    # result1 = get_item_from_list_lbyl(testlist, 5)
    # result1 = get_item_from_list_lbyl(testlist2, 'a')
    # result1 = get_item_from_list_lbyl(testlist2, 3.5)
    # result1 = get_item_from_list_lbyl(testlist2, [1])
    # print(result1)
    # result2 = get_item_from_list(testlist, 5)
    # result2 = get_item_from_list_lbyl(testlist2, 'a')
    # result2 = get_item_from_list_lbyl(testlist2, 3.5)
    # result2 = get_item_from_list_lbyl(testlist2, [1])
    # print(result2)
    return None

"""Change the three functions below from Look Before You Leap (LBYL) to Easier
to Ask for Forgiveness than Permission (EAFP)"""


# Returns the addition of x and y if it's defined, otherwise returns 0
def add_lbyl(x, y):
    if type(x) is str and (type(y) is int or type(y) is float):
        return 0
    elif type(y) is str and (type(x) is int or type(x) is float):
        return 0
    return x + y


# Deze versie van add(x,y) werkt eigenlijk niet goed voor de foute input add(['aha'], 3): deze heeft ten onrechte 
# ook de uitkomst 0, terwijl er eigenlijk een foutmelding moet volgen, om volledig gelijk te zijn
# aan de add_lbyl-versie. Deze versie wordt in wincpy check echter afgekeurd met een rood duimpje. 
def add(x, y):
    try:
        return x+y
    except TypeError:
        return 0

'''
### Onderstaande versie werkt ook goed voor voorbeeld add(['aha'], 3): hier volgt dan zelfde foutmelding als
# bij de add_lbyl-versie. Deze versie wordt in wincpy check echter afgekeurd met een rood duimpje.  
def add(x, y):
    try:
        return x + y
    # except TypeError:
    #     return 0
    except TypeError as e:
        message = str(e)
        if ('unsupported operand type(s)' in message) and (not 'list' in message):
            return 0
        if 'can only concatenate str (not "int") to str' in message:
            return 0
        if 'can only concatenate str (not "float") to str' in message:
            return 0
        else:
            # print('other kind of exception')
            raise 
'''

# Returns the contents of the file at 'filename', or an empty string if the
# file does not exist
'''
def read_file_lbyl(filename):
    if os.path.exists(filename):
        return open(filename, 'r').read()
    else:
        return ''
'''

def read_file(filename):
    # f = None
    try:
        opened_file = open(filename)     
        f = opened_file.read()
        opened_file.close()
        return f
    except FileNotFoundError:
        return ''
    # finally:
    #     if f:
    #         print("Closing file", opened_file.name)
    #         opened_file.close()


# Returns item at `index` from list `l` if possible, otherwise returns None
def get_item_from_list_lbyl(l, index):
    max_index = len(l) - 1
    min_index = -1 - max_index
    if index <= max_index and index >= min_index:
        return l[index]
    else:
        return None


def get_item_from_list(l, index):
    try:
        return l[index]
    except IndexError:
        return None


if __name__ == '__main__':
    main()
