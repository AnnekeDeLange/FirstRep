# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# DEEL 1 OPDRACHT
scoring_player1 = 'Ruud Gullit'
scoring_player2 = 'Marco van Basten'
goal_0 =  32
goal_1 =  54
# scorers_old = scoring_player1 + ' scored in the ' + str(goal_0) + 'nd minute, ' + scoring_player2 + 'scored in the ' + str(goal_1) + 'th minute'
scorers = scoring_player1 + ' ' + str(goal_0) + ', ' + scoring_player2 + ' ' + str(goal_1)
# print(scorers)
report = (f'{scoring_player1} scored in the {goal_0}nd minute\n{scoring_player2} scored in the {goal_1}th minute')
# print(report)
# report_variant2 = (f'''{scoring_player1} scored in the {goal_0}nd minute, 
# {scoring_player2} scored in the {goal_1}th minute.''')
# print(report_variant2)

# DEEL 2 OPDRACHT
player = 'Anatolly Demyanenko'
first_name = player[0:player.find(' ')]
# print(first_name)
last_name_len = len(player[player.find(' ')+1:])
# print(len(first_name))
# print(last_name_len)
name_short = (f'{first_name[0:1]}. {player[len(first_name)+1:]}')
# print(name_short)
## chant_part = (first_name +'! ')*8
## print(chant_part)
chant = ((first_name +'! ') * (len(first_name)-1)) + (first_name +'!')
# print(chant)
good_chant = (chant[len(chant)-1]) != ' '
print(good_chant)
