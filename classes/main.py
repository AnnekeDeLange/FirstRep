# Do not modify these lines

__winc_id__ = '04da020dedb24d42adf41382a231b1ed'

__human_name__ = 'classes'


# Add your code after this line

class Player:
    def __init__(self, name, speed, endurance, accuracy):
        # first ensure the proper type and range of provided values for speed, enducrance and accuracy
        self.test_speed = float(speed)
        self.test_endurance = float(endurance)
        self.test_accuracy = float(accuracy)
        # check range
        if not( (0 < self.test_speed <=1) and (0 < self.test_endurance <=1) and  (0 < self.test_accuracy <=1) ):
            raise ValueError()
        # if check ok then assign the provided values to instance attributes          
        else:
            self.name = name
            self.speed = speed
            self.endurance = endurance
            self.accuracy = accuracy

    def introduce(self):
        introduction_text = f'Hello everyone, my name is {self.name}.'
        return introduction_text

    def strength(self):
        speed_value = self.speed
        endurance_value = self.endurance
        accuracy_value = self.accuracy
        # find highest; if highest value is shared, priority is: speed > endurance > accuracy
        if ( speed_value >= endurance_value and speed_value >= accuracy_value ):
            result = tuple(('speed', self.speed))
        elif (endurance_value >= accuracy_value):
            result = tuple(('endurance', endurance_value))
        else:
            result = tuple(('accuracy', self.accuracy))
        return result


class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        # getattr(object, 'x') is completely equivalent to object.x.
        speed = getattr(player, 'speed')
        endurance = getattr(player, 'endurance')
        accuracy = getattr(player, 'accuracy')
        sum = speed + endurance + accuracy
        return sum

    def compare_players(self, player1, player2, quality):
        quality_1st_player = getattr(player1, quality)
        quality_2nd_player = getattr(player2, quality)
        # what player scores the highest on the specified quality
        if quality_1st_player > quality_2nd_player:
            return player1.name
        elif quality_1st_player < quality_2nd_player:
            return player2.name
        # if they score equally on the specific quality, who has the better specific strength
        else:
            specific_strength_player1 = list(player1.strength())[1]
            specific_strength_player2 = list(player2.strength())[1]
            if  specific_strength_player1 > specific_strength_player2:
                return player1.name
            elif specific_strength_player1 <  specific_strength_player2:
                return player2.name
            else:
                general_strength_player1 = Commentator.sum_player(self, player1)
                general_strength_player2 = Commentator.sum_player(self, player2)
                if  general_strength_player1 > general_strength_player2:
                    return player1.name
                elif general_strength_player1 <  general_strength_player2:
                    return player2.name
                else:
                    # the players score also equal on general strength
                    return f'These two players might as well be twins!'


### test opdracht 1.2 - make player
# player1 = Player('johan', 0.4, 0.3, 0.4)
# player2 = Player('peet', 0.1, 0.45, 0.3)
# player3 = Player('Julie', 0.5, 0.12, 0.5134)

# print(player1.name)
# print(player2.name)
# print(player3.name, 'has speed', player3.speed)

### test opdracht 1.3 - introduce
# print(player3.introduce())

### test opdracht 1.4 - strngth
# print(player1.strength())
# print(player2.strength())
# print(player3.strength())
# print(type(player3.strength()))

### gtest opdracht 2.2 - make commentator
# william = Commentator('William Becket')
# print(william.name)

### test opdracht 2.3 - sum_player
# print( Commentator.sum_player(Commentator, player3) )

### test opdracht 2.4 - compare_player
# player1 = Player('johan', 0.1, 0.1, 0.1)
# player2 = Player('peet', 0.1, 0.45, 0.8)
# player3 = Player('julie', 0.1, 0.7, 0.1)
# print( Commentator.compare_player(Commentator, 'speed', player2, player3) )
