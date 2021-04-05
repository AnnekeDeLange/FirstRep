from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'


# hereafter Part 1 While-exercise
def unique_koala_facts(number):
    unique_facts = []
    i = 1
    go_on = True
    while go_on == True:
        if i > 300:
            go_on = False
        if len(unique_facts) == number:
            break
        else:
            new_fact = str(random_koala_fact())
            if new_fact in unique_facts:
                i += 1
                continue
            else:
                unique_facts.append(new_fact)
                i += 1
    return unique_facts

# hereafter  Part 2 - While-exercise

def update_joey_facts_found(element, elements_list):
    updated = False
    # if elements_list == []:
    #     elements_list.append([element, 1])
    #     updated = True
    for i in range(0, len(elements_list)):
        if elements_list[i][0] == element:
            is_present = True
            counter = elements_list[i][1] + 1
            elements_list[i][1] = counter
            updated = True
            i = i + 1
        else:
            i = i + 1
            continue
    if updated == False:
        elements_list.append([element, 1])
    return elements_list

def enough_unique_joey_facts(nested_list_with_facts, list_facts_seen_enough):
    not_yet_ready = False
    for i in range(0,len(nested_list_with_facts)):
        if nested_list_with_facts[i][1] == 10:
            list_facts_seen_enough.append(nested_list_with_facts[i][0])
        if nested_list_with_facts[i][1] != 10:
            not_yet_ready = True
        else:
            i = i + 1
    if not_yet_ready == True:
        ready = False
    else:
        ready = True  
    return ready

def num_joey_facts():
    joey_facts_found = []
    joey_facts_seen_enough = []
    i = 1
    go_on = True
    while go_on == True:
        if i > 1000:
            go_on = False
            break
        generated_fact = str(random_koala_fact())
        if not 'joey' in generated_fact:
            i += 1
            continue
        elif generated_fact in joey_facts_seen_enough:
            i = i + 1
            continue
        else:
            update_joey_facts_found(generated_fact, joey_facts_found)
            if enough_unique_joey_facts(joey_facts_found, joey_facts_seen_enough) == True:
                go_on = False
                break
            else:
                i += 1
                continue
    # print('joey_facts_found: ', joey_facts_found)
    result = len(joey_facts_found)
    return result


# hereafter Part 3 - While-exercise
def koala_weight():
    i = 1
    go_on = True
    while go_on == True:
        if i > 300:
            go_on = False
        else:
            weight_fact = str(random_koala_fact())
            if 'weigh' and 'kg' in weight_fact:
                go_on = False
            else:
                i += 1
                continue
    kg_index = weight_fact.find('kg')
    weight_index = weight_fact.rfind(' ', 0, kg_index)
    weight = int( weight_fact[weight_index:kg_index] )
    return weight


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    print(random_koala_fact())

    # CALL for While-exercise Part1
    print(unique_koala_facts(150))
    
    ## CALL for While-exercise Part2    
    print(num_joey_facts())
    
    # CALL for While-exrercise Part 3
    print(koala_weight())
