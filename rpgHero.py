class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        # TODO: store `name` and `hp` as INSTANCE attributes
        pass

    def take_damage(self, amount):
        self.hp -= amount
        # TODO: subtract `amount` from this hero's hp
        pass

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(arthur.hp)    
print(morgana.hp)  