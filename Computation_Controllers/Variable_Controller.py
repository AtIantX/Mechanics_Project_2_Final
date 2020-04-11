from random import randrange, random

class VariableController:

    g = 10

    def __init__(self):
        # Not taking into account mass 0
        self.mass_range = (1, 10)
        # ToDo Change to (0, 0.5)
        self.friction_range = (0, 1)
        self.external_force_range = (-300, 300)

    def get_random_mass(self):
        mass = randrange(*self.mass_range)
        return mass

    def get_random_friction(self):
        friction = random()
        return friction

    def get_random_external_force(self):
        external_force = randrange(*self.external_force_range)
        return external_force
