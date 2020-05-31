class Annie:
    def __init__(self, **kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.AP = kwargs['ability_power']

    def tibbers(self):
        tibber = self.AP * 0.65 + 400
        print('티버: 피해량 {}'.format(tibber))


health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()