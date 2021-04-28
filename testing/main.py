
def get_none():
    result = None
    return result


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


# backup before building recursion

def flatten_dict(input_dict):
    # check datatype
    if not type(input_dict) == dict:
        flat_list_result = ['Input was not a dictionary, therefor could not flatten.']
    # simple flatten
    else:
        flat_list_result = list(dict.values(input_dict))
    print(flat_list_result)
    return flat_list_result

print(flatten_dict({'a': [{'inner_inner_a': 42}]}))

#### below attempt for recursive function - version called dict_flatten2
# dict_flatten2 calls a recursive function dict_flatten_recursive

# def flatten_dict_recursive(input, recursion_number, result_upto_now):
#     print('result_upto_now', result_upto_now)
#     print('recursion_number', recursion_number)
#     # Base case and exit condition
#     if (input == {} or input == [] ):
#         result = result_upto_now
#         # return result
#     # Base case and initial input not a dictionary
#     elif ( type(input) != dict) and (recursion_number == 1):
#         result = ['Nothing to flatten because Input is not a dictionary.']
#         # return result
#     # Recursive case
#     else:
#         # initialize in first recursion
#         if recursion_number == 1:
#             result_upto_now = []
#         # peel of dictionary from list and 
#         if type(input) == list:
#             list_to_pass = []
#             for element in input:
#                 if type(element) == dict:
#                     flatten_dict_recursive(element, (recursion_number + 1), result_upto_now)
#                 # else:
#                 #     list_to_pass.append(element)
#                 else:
#                     if element != []:
#                         if type(element) == dict:
#                             flatten_dict_recursive(element, (recursion_number + 1), result_upto_now)
#                         else:
#                             result_upto_now.append(element)
#         # nothing to peel
#         else:
#             if type(input) in [str, float, int, bool]:
#                 result_upto_now.append(list_to_pass)
#             else:
#                 dict_contents = dict.values(input)
#                 # cycle_result = []
#                 # next_cycle_input = []
#                 for element in dict_contents:
#                     if type(element) == dict:
#                         print('again dict encounterd', element)
#                         print('in-else element is dict - result_upto_now ', result_upto_now)
#                         next_recursion = recursion_number + 1
#                         print('next_recursion ', next_recursion)
#                         flatten_dict_recursive(element, next_recursion, result_upto_now)
#                     elif type(element) == list:
#                         list_to_pass = []
#                         if element != []:
#                             print('again list encounterd', element)
#                             print('in-else element is list - result_upto_now ', result_upto_now)
#                             if element == dict:
#                                 next_recursion = recursion_number + 1
#                                 print('next_recursion ', next_recursion)
#                                 print('element for nex recursion', element)
#                                 flatten_dict_recursive(element, (next_recursion), result_upto_now)
#                             elif len(element) == 1:
#                                 single_value = element
#                                 result_upto_now.append(single_value)
#                             else:
#                                 for i in element:
#                                     list_to_pass.append(i)
#                             result_upto_now.append(list_to_pass)
#                     else:
#                         result_upto_now.append(element)
#                         # print('dict-element added in else-else ', result_upto_now)
#     result = result_upto_now
#     return result

# def flatten_dict(dictionary):
#     return flatten_dict_recursive(dictionary, 1, [])


# ## test statements


# print('result1', flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}))

# print('result2', flatten_dict({'a': [{'inner_inner_a': 42}]}))

# print(flatten_dict({'a': [ {'inner_inner_a': 14}, 'nested_2', 'nested_3'], 'c': 16 }))

# print(flatten_dict({'children': ['Ralph', 'Betty', 'Joey'],
#                 'pets': {'dogs': 
#                             {'terriers': ['Fido', 'Bonzo'],
#                             'retrievers': ['Devil', 'Angel']},
#                             'cat': 'Sox' },
#                         'house_in': 'Netherlands',
#                 'income_class': '1.5 - 2.5' }))
