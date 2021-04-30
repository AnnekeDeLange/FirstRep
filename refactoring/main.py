__winc_id__ = '9920545368b24a06babf1b57cee44171'
__human_name__ = 'refactoring'


class Homeowner():

    def __init__(self, name, adress, needs, contracts):
        self.name = name
        self.adress = adress
        self.needs = needs
        self.contracts = contracts

    def match_contracts(self, Specialists):
        for specialist in Specialists:
            profession = getattr(specialist, 'profession')
            if profession in self.needs:
                specialist_name = getattr(specialist, 'name')
                self.contracts.append(specialist_name)
        return self.contracts


class Specialist():

    def __init__(self, name):
        self.name = name


class Electrician(Specialist):
    def __init__(self, name):
        super().__init__(name)
        self.profession = 'electrician'


class Painter(Specialist):
    def __init__(self, name):
        super().__init__(name)
        self.profession = 'painter'


class Plumber(Specialist):
    def __init__(self, name):
        super().__init__(name)
        self.profession = 'plumber'


alfred = Homeowner('Alfred Alfredson',
                   'Alfredslane 123',
                   ['painter', 'plumber'], [])
bert = Homeowner('Bert Bertson', 'Bertslane 231', ['plumber'], [])
candice = Homeowner('Candice Candicedottir',
                    'Candicelane 312',
                    ['electrician', 'plumber'], [])

bob = Painter('Bob Bobsville')
craig = Plumber('Craig Craigsville')
alice = Electrician('Alice Aliceville')


specialists = [bob, craig, alice]

print("Alfred's contracts:", alfred.match_contracts(specialists))
print("Bert's contracts:", bert.match_contracts(specialists))
print("Candice's contracts:", candice.match_contracts(specialists))


# niet meer afgemaakt, ivm tijdsgebrek
'''
    def match_contracts(self, Specialists):
        for specialist in Specialists:
            profession = getattr(specialist, 'profession')
            if profession in self.needs:
                specialist_name = getattr(specialist, 'name')
                self.contracts.append(specialist_name)
        return self.contracts

    def pick_best_offer(self):
        if self.contracts == []:
            return self.contracts
        else:
            specialists_to_compare = self.contracts[0]
            for i in range(1,len(self.contracts)-1):
                to_compare = [self.contracts[0]]
                profession = getattr(self, 'profession')
                if specialist.profession ==
            else:
                for specialist in self.contracts:
                    specialist
'''
