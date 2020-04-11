# def main_controller:


class ComputationEngine:
    object1, object2, object3 = None, None, None
    acceleration_2, acceleration_1 = 0, 0
    g, external_force = 0, 0

    def __init__(self, object1, object2, object3, g, external_force):
        ComputationEngine.object1 = object1
        ComputationEngine.object2 = object2
        ComputationEngine.object3 = object3
        ComputationEngine.g = g
        ComputationEngine.external_force = external_force

    def compute(self, t_f_cor):
        obj1 = ComputationEngine.object1
        obj2 = ComputationEngine.object2
        obj3 = ComputationEngine.object3
        for pair in t_f_cor:
            ComputationEngine.acceleration_2 = ComputationEngine.compute_acceleration_2(obj1.weight, obj2.weight,
                                                                                        obj3.weight, obj1.friction,
                                                                                        obj2.friction, obj3.friction,
                                                                                        ComputationEngine.g,
                                                                                        pair[1])
            ComputationEngine.acceleration_1 = ComputationEngine.compute_acceleration_1(
                ComputationEngine.acceleration_2, obj1.weight, obj2.weight, obj1.friction, obj2.friction,
                ComputationEngine.g)
            self.update_objects(pair[0], ComputationEngine.acceleration_1, ComputationEngine.acceleration_2)


    @staticmethod
    def compute_accelaration():
        obj1 = ComputationEngine.object1
        obj2 = ComputationEngine.object2
        obj3 = ComputationEngine.object3
        # First of all compute acceleration2
        ComputationEngine.acceleration_2 = ComputationEngine.compute_acceleration_2(obj1.weight, obj2.weight,
                                                                                    obj3.weight, obj1.friction,
                                                                                    obj2.friction, obj3.friction,
                                                                                    ComputationEngine.g,
                                                                                    ComputationEngine.external_force)
        ComputationEngine.acceleration_1 = ComputationEngine.compute_acceleration_1(ComputationEngine.acceleration_2,
                                                                                    obj1.weight, obj2.weight,
                                                                                    obj1.friction, obj2.friction,
                                                                                    ComputationEngine.g)
        return [obj1.weight, obj2.weight, obj3.weight, obj1.friction, obj2.friction, obj3.friction, ComputationEngine.g,
                ComputationEngine.external_force, ComputationEngine.acceleration_2, ComputationEngine.acceleration_1]

    def update_objects(self, t, acc1, acc2):
        # Update Object 1
        self.object1.move_coordinate_x(self.compute_coordinate_shift(self.object1.velocity, acc1, t))
        self.object1.velocity = self.compute_velocity(self.object1.velocity, acc1, t)
        print(self.object1.pos, "Coordinates of Object 1 at time " + str(t) + "s")
        # Update Object 2
        self.object2.move_coordinate_x(self.compute_coordinate_shift(self.object2.velocity, acc2, t))
        self.object2.velocity = self.compute_velocity(self.object2.velocity, acc2, t)
        print(self.object2.pos, "Coordinates of Object 2 at time " + str(t) + "s")
        # Update Object 3
        self.object3.move_coordinate_y(self.compute_coordinate_shift(self.object3.velocity, acc2, t))
        self.object3.move_coordinate_x(self.compute_coordinate_shift(self.object1.velocity, acc1, t))
        self.object3.velocity = self.compute_velocity(self.object3.velocity, acc2, t)
        print(self.object3.pos, "Coordinates of Object 3 at time " + str(t) + "s")

    @staticmethod
    def compute_acceleration_2(m1, m2, m3, f1, f2, f3, g, external_force):
        acc = (-1*(m1+m3)*(f2*m2*g - m3*g + 2*f3*external_force) + m3*(f2*m2*g - f1*m1*g + f1*f2*m2*g))/(m2*(m1+m3) - m3*(-1*m2 + f1*m2 - m1 - m3))
        return acc

    @staticmethod
    def compute_acceleration_1(a2, m1, m2, f1, f2, g):
        acc = (-1*m2*a2 + f2*m2*g - f1*m1*g + f1*m2*a2 + f1*f2*m2*g)/(m1+m2)
        return acc

    @staticmethod
    def compute_coordinate_shift(v_0, a, t):
        shift = v_0*t + (a*pow(t, 2))/2
        return shift

    @staticmethod
    def compute_velocity(v_0, a, t):
        velocity = v_0*t + a*t
        return velocity
