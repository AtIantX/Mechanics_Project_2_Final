# Main Controller
from Computation_Controllers.Simulation_Controller import Simulation
from Computation_Controllers.CSV_controller import CSVController
from Computation_Controllers.Visualization_Controller import VisualizationController
from Computation_Controllers.Prediction_Controller import Prediction


class MainController:
    simulation = None
    csv_controller = None
    visualisation_controller = None
    prediction = None


    def __init__(self):
        MainController.simulation = Simulation()
        MainController.csv_controller = CSVController()
        MainController.visualisation_controller = VisualizationController()
        MainController.prediction = Prediction()

    @staticmethod
    def test_acceleration():
        result = MainController.simulation.start_acceleration_computation_simulation()
        print(result)

    @staticmethod
    def collect_acceleration_data(test_number):
        header = ["Mass_1", "Mass_2", "Mass_3", "Friction_1", "Friction_2", "Friction_3", "g", "External_Force",
                  "Acceleration of Object 1", "Acceleration of Object 2/3"]
        acceleration_data = []
        for _ in range(test_number):
            result = MainController.simulation.start_acceleration_computation_simulation()
            acceleration_data.append(result)
        MainController.csv_controller.write_csv("Simulation_results/force_acceleration.csv", acceleration_data, header)

    @staticmethod
    def start_simulation(data):
        MainController.simulation.start_simulation(data)

    @staticmethod
    def show_plots():
        MainController.visualisation_controller.visualise_connection("force_acc", "External_Force", "Acceleration of Object 2/3")

    @staticmethod
    def predict_acceleration(force):
        res = MainController.prediction.predict_acceleration(force)
        print(res)


if __name__ == "__main__":
    # Give time_force_data
    time_force_connection = [[0, 300], [1, 200], [2, 100], [3, 0]]

    main_controller = MainController()
    # main_controller.test_acceleration()
    # Uncomment next line to generate data into CSV File
    # main_controller.collect_acceleration_data(1000)

    # Another File with constant masses and frictions but changing external force is logged on force_acceleration.csv
    # main_controller.collect_acceleration_data(1000)

    # See connection between force and acceleration
    main_controller.show_plots()

    # Predict acceleration
    main_controller.predict_acceleration(250)

    MainController.start_simulation(time_force_connection)

