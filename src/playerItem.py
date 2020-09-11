class PlayerItems:
    def __init__(self, name, description, value):
        self.name = name
        self.descrition = description


def __str__(self):
    return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(PlayerItems):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)


class Branch(Weapon):
    def __init__(self):
        super().__init__(name="Branch",
                         description="a large brach with a handle to swing it around with",
                         value=10,
                         damage=30)


class Rustymachete(Weapon):
    def __init__(self):
        super().__init__(name='Rusty Machete',
                         description='a rusty machete someone dropped on the ground, looks very old',
                         value=15,
                         damage=80)


class SwitchAxe(Weapon):

    def __init__(self):
        super().__init__(name="Swith Axe",
                         description='A giant axe that transforms into a giant sword',
                         value=100,
                         damage=350)


class OtherItems(PlayerItems):

    def __init__(self, name, decription, value, effect):
        self.effect = effect
        super().__init__(name, decription, value)


class Lantern(OtherItems):
    def __init__(self):
        super().__init__(name='Lantern',
                         decription='a lantern you found in a cave that seems to shine forever',
                         value=100,
                         effect="lights the path")
