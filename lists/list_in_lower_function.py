def list_in_lower(list,index):
    if index == int(len(list)):
        return list
    else:
#        print(index)
        to_lower = list.pop(index)
#        print(to_lower)
        lowered = to_lower.lower()
#        print(lowered)
        list.insert(index, lowered)
        list_in_lower(list,index+1)
        return list

print(list_in_lower(['Jaws', 'Star Wars: Episode IV – A New Hope', 
                                'E.T. the Extra-Terrestrial',
                                'Memoirs of a Geisha'],0))
