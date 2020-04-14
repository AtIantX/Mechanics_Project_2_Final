# Description of physical object in the problem
from .Variable_Controller import VariableController

class PhysicalObject:

    def __init__(self):
        self.var_controller = VariableController()
        self.weight = 0
        self.friction = 0
        self.pos = [0, 0]
        self.velocity = 0

    def move_coordinate_x(self, x):
        self.pos[0] = self.pos[0] + x

    def move_coordinate_y(self, y):
        self.pos[1] = self.pos[1] + y

    def update_object(self):
        self.weight = self.var_controller.get_random_mass()
        self.weight = self.var_controller.get_random_friction()
