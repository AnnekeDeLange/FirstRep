# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cow_milking_needed, cow_location, season, slurry_tank_full, grass_long):
    if (
        str(weather) not in ['rainy', 'sunny', 'windy', 'neutral'] or
        str(time_of_day) not in ['day', 'night'] or
        str(cow_location) not in ['pasture', 'cowshed'] or
        str(season) not in ['winter', 'spring', 'summer', 'fall'] 
        ):
        return 'wait'
    elif ( 
        cow_location == 'pasture' and
        (weather == 'rainy' or time_of_day == 'night')
        ):
        return 'take cows to cowshed'
    elif cow_milking_needed == True:
        if  cow_location == 'pasture':
            return f'take cows to cowshed\n'+'milk cows\n'+'take cows back to pasture'
        else: return 'milk cows'
    elif (
        slurry_tank_full == True and 
            weather not in ['sunny', 'windy'] 
        ):
        if cow_location == 'pasture':
            return f'take cows to cowshed\n'+'fertilize pasture\n'+'take cows back to pasture'
        else: 
            return 'fertilize pasture'
    elif ( 
        grass_long == True and 
        season == 'spring' and 
        weather == 'sunny'
        ):
        if  cow_location == 'pasture':
            return f'take cows to cowshed\n'+'mow grass\n'+'take cows back to pasture'
        else: return 'mow grass'
    else:
        return 'wait'

# farm_action('sunny','night',True,'pasture','autumn',False, True) #test input valid
# farm_action('sunny','night',True,'pasture','fall',True, True)
# farm_action('sunny', 'day', True, 'pasture', 'spring', False, True) # test example 4 
# farm_action('windy', 'night', True, 'cowshed', 'winter', True, True) # test example 3
# farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True) # test example 2
# farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True) # test example 1
# farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)