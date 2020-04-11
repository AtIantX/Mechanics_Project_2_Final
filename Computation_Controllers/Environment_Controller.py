# Simulation of Physical Environment
from .ObjectModel import PhysicalObject
from .Variable_Controller import VariableController


class Environment:
    var_controller = VariableController()
    object1, object2, object3, g, external_force = None, None, None, None, None

    def __init__(self):
        self.generate_objects()
        self.get_global_variables()
        self.prepare_objects()

    @staticmethod
    def generate_objects():
        Environment.object1 = PhysicalObject()
        Environment.object2 = PhysicalObject()
        Environment.object3 = PhysicalObject()

    @staticmethod
    def get_global_variables():
        Environment.g = VariableController.g
        Environment.external_force = Environment.var_controller.get_random_external_force()

    @staticmethod
    def prepare_objects():
        Environment.object1.weight, Environment.object2.weight, Environment.object3.weight = Environment.var_controller.get_random_mass(), Environment.var_controller.get_random_mass(), Environment.var_controller.get_random_mass()
        Environment.object1.friction, Environment.object2.friction, Environment.object3.friction = Environment.var_controller.get_random_friction(), Environment.var_controller.get_random_friction(), Environment.var_controller.get_random_friction()


