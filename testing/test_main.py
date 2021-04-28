# test_main

from main import get_none
from main import flatten_dict

'''
def test_get_none():
    test_result_0 = get_none()
    assert test_result_0 == None
'''

# testcases for flatten_dict(dict)

test_no_list_1 = 'a'
test_no_list_2 = (1,2,3)
test_no_list_3 = 1
test_no_list_4 = {'a': 42, 'b': 3.14}

test_dict_1 = {'bob': 10, 'sharon': 9, 'eli': 10}
test_dict_2_1 = {'a': 42, 'b': 3.14}
test_dict_2_2 = {'a': [42, 350], 'b': 3.14}
test_dict_3 = {'dog': 'Fido', 'cat': 'Sox'}
test_dict_4 = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
test_dict_5 = {'children' : ['Ralph', 'Betty', 'Joey'], 
                'pets': {'dog': 'Fido', 'cat': 'Sox'}}
test_dict_6 = {'children': ['Ralph', 'Betty', 'Joey'],
                'pets': {'dogs': 
                            {'terriers': ['Fido', 'Bonzo'],
                            'retrievers': ['Devil', 'Angel']},
                            'cat': 'Sox' },
                        'house_in': 'Netherlands',
                'income_class': '1.5 - 2.5' }
test_nested_dict_7 = {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}
test_nested_dict_8 = {'a': [{'inner_inner_a': 42}]}
test_nested_dict_9 = {'a': [ {'inner_inner_a': 14}, 'nested_2', 'nested_3'], 'c': 16 }


## tests for simple flatten

def test_flatten_dict_is_list():
    result = flatten_dict(test_no_list_2)
    assert type(result) == list

def test_flatten_dict_simple_1():
    assert flatten_dict(test_dict_1) == [10, 9, 10]

def test_flatten_dict_simple_2_1():
    assert flatten_dict(test_dict_2_1) == [42, 3.14]

def test_flatten_dict_simple_2_2():
    assert flatten_dict(test_dict_2_2) == [ [42,350], 3.14]

def test_flatten_dict_simple_3():
    assert flatten_dict(test_dict_3) == ['Fido','Sox']

def test_flatten_dict_simple_4():
    assert flatten_dict(test_dict_4) == ['a','b','c','d']

def test_flatten_dict_mixed_datatypes_1():
        assert flatten_dict(test_dict_5) == [
             ['Ralph', 'Betty', 'Joey'],
             {'dog': 'Fido', 'cat': 'Sox'}
             ]

def test_flatten_dict_mixed_datatypes_2():
        assert flatten_dict(test_dict_6) == [
            ['Ralph', 'Betty', 'Joey'],
            {'dogs': {'terriers': ['Fido', 'Bonzo'],
                            'retrievers': ['Devil', 'Angel'] },
             'cat': 'Sox' },
            'Netherlands',
            '1.5 - 2.5'
             ]


def test_flatten_mixed_datatypes_3():
     assert flatten_dict(test_nested_dict_7) == [
         {'inner_a': 42, 'inner_b': 350},
         3.14
         ]


def test_flatten_dict_mixed_datatypes_2():
        assert flatten_dict(test_dict_6) == [
            ['Ralph', 'Betty', 'Joey'],
            {'dogs': {'terriers': ['Fido', 'Bonzo'],
                            'retrievers': ['Devil', 'Angel'] },
             'cat': 'Sox' },
            'Netherlands',
            '1.5 - 2.5'
             ]

def test_flatten_dict_nested_1():
    assert flatten_dict(test_nested_dict_7) == [{'inner_a': 42, 'inner_b': 350}, 3.14]

def test_flatten_dict_nested_2():
    assert flatten_dict(test_nested_dict_8) == [ [{'inner_inner_a': 42}] ]

def test_flatten_dict_nested_3():
     assert flatten_dict(test_nested_dict_9) == [ [{'inner_inner_a': 14}, 'nested_2', 'nested_3'], 16]


### tests for recursive flatten

'''
def test_flatten_dict_is_list():
    result = flatten_dict(test_no_list_2)
    assert type(result) == list

def test_flatten_dict_simple_1():
    assert flatten_dict(test_dict_1) == [10, 9, 10]

def test_flatten_dict_simple_2_1():
    assert flatten_dict(test_dict_2_1) == [42, 3.14]

def test_flatten_dict_simple_2_2():
    assert flatten_dict(test_dict_2_2) == [ [42,350], 3.14]

def test_flatten_dict_simple_3():
    assert flatten_dict(test_dict_3) == ['Fido','Sox']

def test_flatten_dict_simple_4():
    assert flatten_dict(test_dict_4) == ['a','b','c','d']

def test_flatten_dict_mixed_datatypes_1():
        assert flatten_dict(test_dict_5) == [
             ['Ralph', 'Betty', 'Joey'],
             ['Fido', 'Sox']
             ]

def test_flatten_dict_mixed_datatypes_2():
        assert flatten_dict(test_dict_6) == [
            ['Ralph', 'Betty', 'Joey'],
            [ ['Fido', 'Bonzo'], ['Devil', 'Angel'], 'Sox'],
            'Netherlands',
            '1.5 - 2.5'
             ]


def test_flatten_mixed_datatypes_3():
     assert flatten_dict(test_nested_dict_7) == [[42, 350], 3.14]


def test_flatten_dict_mixed_datatypes_2():
        assert flatten_dict(test_dict_6) == [
            ['Ralph', 'Betty', 'Joey'], 
            [ ['Fido', 'Bonzo'], ['Devil', 'Angel'], 'Sox' ],
            'Netherlands', '1.5 - 2.5'
            ]

def test_flatten_dict_nested_1():
    assert flatten_dict(test_nested_dict_7) == [ [42, 350], 3.14]

def test_flatten_dict_nested_2():
     assert flatten_dict(test_nested_dict_8) == [42]

def test_flatten_dict_nested_3():
     assert flatten_dict(test_nested_dict_9) == [ [ [14], 'nested_2', 'nested_3'], 16]
'''