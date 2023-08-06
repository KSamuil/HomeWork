class SuperHero:
    people = 'people'

    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase

    def Name_Hero(self):
        return (f'Hero`s name: {self.name}')

    def Health_is_double(selfs):
        selfs.health_points *= 2

    def __str__(self):
        return (f'NickName: {self.nickname}\nSuperPower: {self.superpower}\nHealthPoints: {self.health_points}')

    def __len__(self):
        return len(self.catchphrase)

Hero=SuperHero(name='Samael', nickname='Angel', superpower='Flight', health_points=500,catchphrase='deus lo vult')

print(Hero.Name_Hero())
print(f'HealthPoints before: {Hero.health_points}')
Hero.Health_is_double()
print(f'Health points after doubling: {Hero.health_points}')
print(str(Hero))
print(f'Catchphrase length: {len(Hero)}')
